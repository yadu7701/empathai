from flask import Flask, request, jsonify, render_template, Response
import cv2
from deepface import DeepFace
from ultralytics import YOLO
import time
from collections import deque
from threading import Lock
import logging
import torch
import ollama
import os

app = Flask(__name__)

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Initialize the video capture object
if 'PYTHONANYWHERE_DOMAIN' in os.environ:
    # When running on PythonAnywhere, use a demo video or disable camera
    camera = None
    logger.warning("Running on PythonAnywhere - camera disabled")
else:
    # Local development with webcam
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        logger.error("Cannot open webcam")
        exit()

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if face_cascade.empty():
    logger.error("Failed to load Haar cascade classifier.")
    exit()

# Initialize YOLOv8n model with CUDA
try:
    yolo_model = YOLO('yolov8n.pt')  # Automatically uses GPU if available
    if torch.cuda.is_available():
        yolo_model.to('cuda')
        logger.info("YOLOv8n model loaded successfully on GPU.")
    else:
        logger.info("YOLOv8n model loaded successfully on CPU.")
except Exception as e:
    logger.critical(f"Failed to load YOLOv8n model: {e}")
    exit()

# Deque to store emotions with timestamps
emotion_history = deque()
history_lock = Lock()
TIME_WINDOW = 5  # seconds

# Variables to store detected objects
obj1 = None
obj2 = None
obj3 = None

# Add these global variables at the top with other globals
previous_obj1 = None
previous_obj2 = None
person_disappeared = False
conversation_history = []
MAX_HISTORY = 5  # Keep last 5 exchanges

def generate_frames():
    global obj1, obj2, obj3
    frame_count = 0
    while True:
        success, frame = camera.read()
        if not success:
            logger.error("Failed to capture frame from camera.")
            break
        else:
            frame_count += 1
            if frame_count % 5 != 0:
                continue

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            logger.debug(f"Faces detected: {len(faces)}")

            for (x, y, w, h) in faces:
                face_roi = frame[y:y + h, x:x + w]
                try:
                    result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
                    emotion = result[0]['dominant_emotion'] if isinstance(result, list) else result['dominant_emotion']
                    logger.info(f"Detected Emotion: {emotion}")
                except Exception as e:
                    emotion = "Error"
                    logger.error(f"Emotion detection error: {e}")

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

                current_time = time.time()
                with history_lock:
                    emotion_history.append((emotion, current_time))
                    while emotion_history and (current_time - emotion_history[0][1] > TIME_WINDOW):
                        emotion_history.popleft()

            try:
                results = yolo_model(frame)
                detections = results[0].boxes
                obj1 = obj2 = obj3 = None

                for idx, box in enumerate(detections):
                    class_id = int(box.cls[0])
                    label = yolo_model.names[class_id]
                    confidence = box.conf[0].item()

                    if idx == 0:
                        obj1 = label
                    elif idx == 1:
                        obj2 = label
                    elif idx == 2:
                        obj3 = label

                    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            except Exception as e:
                logger.error(f"Object detection error: {e}")

            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                logger.error("Failed to encode frame")
                continue
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('final.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/current_emotion')
def current_emotion():
    with history_lock:
        if not emotion_history:
            emotion = "I can't see you."
        else:
            current_time = time.time()
            # Filter emotions from last 5 seconds
            recent_emotions = [e[0] for e in emotion_history if current_time - e[1] <= 5]
            
            if not recent_emotions:
                emotion = "I can't see you."
            else:
                # Count occurrences of each emotion
                emotion_counts = {}
                for emo in recent_emotions:
                    emotion_counts[emo] = emotion_counts.get(emo, 0) + 1
                # Get the most frequent emotion
                emotion = max(emotion_counts, key=emotion_counts.get)
    return jsonify({"emotion": emotion}), 200

@app.route('/current_objects')
def current_objects():
    global obj1, obj2, obj3
    objects = {
        "obj1": obj1 if obj1 else "None",
        "obj2": obj2 if obj2 else "None",
        "obj3": obj3 if obj3 else "None",
    }
    return jsonify(objects), 200

@app.route('/chat', methods=['POST'])
def chat():
    global obj1, obj2, obj3, previous_obj1, previous_obj2, person_disappeared, conversation_history
    
    user_message = request.json.get("message", "")
    message_type = request.json.get("type", "regular")

    # Get emotion first
    with history_lock:
        if not emotion_history:
            emotion = "I can't see you."
        else:
            current_time = time.time()
            recent_emotions = [e[0] for e in emotion_history if current_time - e[1] <= 5]
            
            if not recent_emotions:
                emotion = "I can't see you."
            else:
                emotion_counts = {}
                for emo in recent_emotions:
                    emotion_counts[emo] = emotion_counts.get(emo, 0) + 1
                emotion = max(emotion_counts, key=emotion_counts.get)

    # Handle initial emotion greeting
    if message_type == "initial_greeting":
        if emotion == "I can't see you.":
            system_message = "I notice I can't see you clearly. Please make sure you're visible in the camera so I can assist you better."
        else:
            system_message = f"I notice that you're feeling {emotion}. How can I help you today?"
        return jsonify({"message": {"content": system_message}}), 200

    # Handle person check
    if message_type == "person_check":
        if (previous_obj1 == "person" or previous_obj2 == "person") and \
           obj1 != "person" and obj2 != "person" and \
           not person_disappeared:
            person_disappeared = True
            system_message = "Hey, I noticed your friend left. I hope everything is okay!"
            return jsonify({"message": {"content": system_message}}), 200
        return jsonify({"message": {"content": ""}}), 200

    # Update previous states
    previous_obj1 = obj1
    previous_obj2 = obj2

    # Reset person_disappeared flag if a person is detected again
    if obj1 == "person" or obj2 == "person":
        person_disappeared = False

    # Handle object detection message
    if message_type == "object_greeting":
        detected_objects = []
        
        # Check each object
        for obj in [obj1, obj2, obj3]:
            if obj and obj.lower() not in ["person", "none", ""]:
                detected_objects.append(obj)
        
        if detected_objects:
            if len(detected_objects) == 1:
                system_message = f"I can see that there's a {detected_objects[0]} in view. Would you like to talk about it?"
            elif len(detected_objects) == 2:
                system_message = f"I can see a {detected_objects[0]} and a {detected_objects[1]}. Would you like to discuss either of them?"
            else:
                system_message = f"I can see several objects: a {', a '.join(detected_objects[:-1])}, and a {detected_objects[-1]}. Which one would you like to talk about?"
            
            return jsonify({"message": {"content": system_message}}), 200
            
        return jsonify({"message": {"content": ""}}), 200

    # Handle regular chat messages
    if message_type == "regular" and user_message:
        system_message = (
            f"You are a helpful assistant who can see the user's face and detect their emotions. "
            f"You are a helpful assistant you can  answer any question. "
            f"you are a helpful assistant who have access to the camera and can see {obj1} {obj2} {obj3} and {emotion}"
            f"Currently, the user appears to be feeling {emotion}. Respond thoughtfully, "
            f"considering that you can see the user's facial expressions."
            f"you are helpful assistant that respond based on {emotion}, if the {emotion} is neutral the reply should be uplifting"
            f"you are helpful assistant that respond based on {emotion}, if the {emotion} is sad try to lighten the mood with the replays"
            f"you are helpful assistant who change tone of replay based on {emotion}"
            f"you are helpful assistant that can see my sarroundings and objects {obj1} {obj2} {obj3}"
            f"you are a helpfull assistant who ask who is the friend if the {obj1} {obj2} is a person"
            f"you are a helpfull assistent who see the objects near me like {obj1} {obj2} {obj3} and answer question about that"
        )

        # Create messages array with conversation history
        messages = [{"role": "system", "content": system_message}]
        
        # Add conversation history
        for msg in conversation_history:
            messages.append(msg)
            
        # Add current user message
        messages.append({"role": "user", "content": user_message})

        # Get response from Ollama
        response = ollama.chat(
            model="nemotron-mini",
            messages=messages
        )

        # Update conversation history
        conversation_history.append({"role": "user", "content": user_message})
        conversation_history.append({"role": "assistant", "content": response["message"]["content"]})
        
        # Keep only last MAX_HISTORY exchanges
        if len(conversation_history) > MAX_HISTORY * 2:  # *2 because each exchange has 2 messages
            conversation_history = conversation_history[-MAX_HISTORY * 2:]

        return jsonify(response), 200

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
