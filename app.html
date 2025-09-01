<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Combined Emotion and Chat Interface</title>
    <style>
        body {
            display: flex;
            justify-content: space-between;
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
        }
        #videoContainer {
            width: 50%;
            text-align: center;
        }
        #chatContainer {
            width: 45%;
            padding: 30px;
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            margin: 20px;
            height: calc(100vh - 40px);
            display: flex;
            flex-direction: column;
        }
        h1 {
            color: #333;
        }
        #currentEmotion, #detectedObjects {
            margin-top: 20px;
            font-size: 1.2em;
            color: #555;
        }
        #detectedObjects ul {
            list-style-type: none;
            padding: 0;
        }
        #detectedObjects li {
            display: inline-block;
            margin: 0 10px;
            padding: 5px 10px;
            background-color: #e0e0e0;
            border-radius: 5px;
        }
        #videoFeed {
            border-radius: 50%;
            object-fit: cover;
            width: 480px;
            height: 480px;
            border: 3px solid #333;
        }
        #videoContainer {
            width: 50%;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .chat-input-container {
            margin-top: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .input-group {
            display: flex;
            gap: 10px;
        }
        input[type="text"] {
            padding: 12px 20px;
            border: 2px solid #e0e0e0;
            border-radius: 25px;
            font-size: 16px;
            flex-grow: 1;
            transition: border-color 0.3s ease;
        }
        input[type="text"]:focus {
            outline: none;
            border-color: #007bff;
        }
        button {
            padding: 12px 30px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #0056b3;
        }
        .chat-response {
            margin-top: 30px;
            background: #f8f9fa;
            padding: 20px;
            border-radius: 15px;
            flex-grow: 1;
            overflow-y: auto;
        }
        .chat-response h3 {
            color: #333;
            margin-bottom: 15px;
            font-size: 1.2em;
        }
        #responseText {
            line-height: 1.6;
            color: #444;
            white-space: pre-wrap;
        }
        .emotion-display {
            margin-top: 15px;
            padding: 10px;
            background: #e3f2fd;
            border-radius: 10px;
            color: #1565c0;
        }
        /* Scrollbar styling */
        .chat-response::-webkit-scrollbar {
            width: 8px;
        }
        .chat-response::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 4px;
        }
        .chat-response::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 4px;
        }
        .chat-response::-webkit-scrollbar-thumb:hover {
            background: #555;
        }
        .chat-history {
            flex-grow: 1;
            overflow-y: auto;
            padding: 20px;
            margin-bottom: 20px;
            background: #f8f9fa;
            border-radius: 15px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        .message {
            max-width: 80%;
            padding: 12px 16px;
            border-radius: 15px;
            margin: 5px 0;
            word-wrap: break-word;
        }
        .user-message {
            background-color: #007bff;
            color: white;
            align-self: flex-end;
            border-bottom-right-radius: 5px;
        }
        .bot-message {
            background-color: #e9ecef;
            color: #333;
            align-self: flex-start;
            border-bottom-left-radius: 5px;
        }
        .message-time {
            font-size: 0.7em;
            margin-top: 5px;
            opacity: 0.7;
        }
        .chat-history::-webkit-scrollbar {
            width: 8px;
        }
        .chat-history::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 4px;
        }
        .chat-history::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 4px;
        }
        .chat-history::-webkit-scrollbar-thumb:hover {
            background: #555;
        }
        #chatContainer {
            width: 45%;
            padding: 30px;
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            margin: 20px;
            height: calc(100vh - 40px);
            display: flex;
            flex-direction: column;
        }
        .chat-input-container {
            margin-top: auto;
            padding-top: 20px;
            border-top: 1px solid #eee;
        }
        .speak-button {
            background: none;
            border: none;
            cursor: pointer;
            font-size: 1.2em;
            padding: 5px;
            margin-left: 5px;
            opacity: 0.7;
            transition: opacity 0.3s;
        }
        .speak-button:hover {
            opacity: 1;
        }
        .bot-message {
            display: flex;
            align-items: center;
            background-color: #e9ecef;
            color: #333;
            align-self: flex-start;
            border-bottom-left-radius: 5px;
        }
        /* Add a mute button to the chat container */
        .audio-control {
            position: absolute;
            top: 10px;
            right: 10px;
            padding: 8px;
            background: none;
            border: none;
            cursor: pointer;
            font-size: 1.5em;
            opacity: 0.7;
            transition: opacity 0.3s;
        }
        .audio-control:hover {
            opacity: 1;
        }
        #voiceButton {
            background-color: #28a745;
            padding: 12px 20px;
        }
        
        #voiceButton.recording {
            background-color: #dc3545;
            animation: pulse 1.5s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        .mic-button {
            background: none;
            border: none;
            padding: 8px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.2s ease;
        }

        .mic-button img {
            width: 24px;
            height: 24px;
        }

        .mic-button.recording {
            animation: pulse 1.5s infinite;
        }

        .mic-button:hover {
            transform: scale(1.1);
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div id="videoContainer">
        <h1>emapathAI</h1>
        <img src="{{ url_for('video_feed') }}" id="videoFeed">
        <div id="currentEmotion">
            Current Emotion: <span id="emotionText">Loading...</span>
        </div>
        <div id="detectedObjects">
            <h3>Detected Objects:</h3>
            <ul>
                <li>Obj1: <span id="obj1Text">Loading...</span></li>
                <li>Obj2: <span id="obj2Text">Loading...</span></li>
                <li>Obj3: <span id="obj3Text">Loading...</span></li>
            </ul>
        </div>
    </div>
    
    <div id="chatContainer">
        <h1></h1>
        
        <div class="chat-history" id="chatHistory">
            <!-- Messages will be dynamically added here -->
        </div>

        <div class="chat-input-container">
            <div class="input-group">
                <input type="text" id="userMessage" placeholder="Type your message here...">
                <button onclick="startVoiceInput()" id="voiceButton" class="mic-button">
                    <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMiAxdjZ2LTZabTQgNmE0IDQgMCAwIDEtOCAwVjdhNCA0IDAgMSAxIDggMHY1WiIvPjxwYXRoIGQ9Ik0xOSAxMHYyYTcgNyAwIDAgMS0xNCAwdi0yTTEyIDE4djR2LTRabTAgNGg0aC00Wm0wIDBoLTRoNFoiLz48L3N2Zz4=" alt="Microphone" id="micIcon">
                </button>
                <button onclick="sendMessage()">Send</button>
            </div>
        </div>
        <button id="audioToggle" class="audio-control" onclick="toggleAudio()">🔊</button>
    </div>

    <script>
        const speechSynthesis = window.speechSynthesis;
        let speaking = false;

        function speakMessage(text) {
            if (speaking) {
                speechSynthesis.cancel();
            }

            const utterance = new SpeechSynthesisUtterance(text);
            
            // Optimize voice parameters for a younger female voice
            utterance.rate = 1.1;      // Slightly faster than default
            utterance.pitch = 1.2;     // Higher pitch for feminine voice
            utterance.volume = 1.0;    // Full volume
            
            // Wait for voices to load
            const voices = speechSynthesis.getVoices();
            
            // Try to find a female English voice
            const femaleVoice = voices.find(voice => 
                voice.name.toLowerCase().includes('female') && 
                voice.lang.startsWith('en')
            ) || voices.find(voice => 
                (voice.name.includes('Samantha') || 
                 voice.name.includes('Alex') ||
                 voice.name.includes('Karen') ||
                 voice.name.includes('Victoria')) && 
                voice.lang.startsWith('en')
            );

            if (femaleVoice) {
                utterance.voice = femaleVoice;
            }

            // Log available voices for debugging
            console.log('Available voices:', voices.map(v => `${v.name} (${v.lang})`));

            speaking = true;
            utterance.onend = () => {
                speaking = false;
            };

            speechSynthesis.speak(utterance);
        }

        // Add this function to initialize voices
        function initVoices() {
            return new Promise((resolve) => {
                if (speechSynthesis.getVoices().length) {
                    resolve();
                } else {
                    speechSynthesis.onvoiceschanged = () => resolve();
                }
            });
        }

        let inactivityTimer;
        let objectDetectionTimer;
        let hasInitialMessageBeenSent = false;
        let hasObjectMessageBeenSent = false;
        let personCheckTimer;
        let isCheckingPerson = false;

        function resetInactivityTimer() {
            clearTimeout(inactivityTimer);
            clearTimeout(objectDetectionTimer);
            if (!hasInitialMessageBeenSent) {
                inactivityTimer = setTimeout(sendInitialMessage, 10000);
            } else if (!hasObjectMessageBeenSent) {
                objectDetectionTimer = setTimeout(sendObjectMessage, 10000);
            }
            
            // Always keep checking for person disappearance
            if (!isCheckingPerson) {
                isCheckingPerson = true;
                personCheckTimer = setInterval(checkPersonPresence, 5000); // Check every 5 seconds
            }
        }

        async function sendInitialMessage() {
            if (hasInitialMessageBeenSent) return;
            
            try {
                const response = await fetch("/chat", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ 
                        message: "",
                        type: "initial_greeting"
                    })
                });

                if (response.ok) {
                    const data = await response.json();
                    const botResponse = data.message?.content;
                    if (botResponse) {
                        addMessageToHistory(botResponse, false);
                        if (autoSpeak) {
                            speakMessage(botResponse);
                        }
                        hasInitialMessageBeenSent = true;
                        objectDetectionTimer = setTimeout(sendObjectMessage, 10000);
                    }
                }
            } catch (error) {
                console.error("Error sending initial message:", error);
            }
        }

        async function sendObjectMessage() {
            if (hasObjectMessageBeenSent) return;
            
            try {
                const response = await fetch("/chat", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ 
                        message: "",
                        type: "object_greeting"
                    })
                });

                if (response.ok) {
                    const data = await response.json();
                    const botResponse = data.message?.content;
                    if (botResponse) {  // Only add message if there's content (meaning non-person objects were found)
                        addMessageToHistory(botResponse, false);
                        if (autoSpeak) {
                            speakMessage(botResponse);
                        }
                        hasObjectMessageBeenSent = true;
                    } else {
                        // If no relevant objects were found, mark as sent but don't show message
                        hasObjectMessageBeenSent = true;
                    }
                }
            } catch (error) {
                console.error("Error sending object message:", error);
            }
        }

        async function sendMessage() {
            clearTimeout(inactivityTimer);
            clearTimeout(objectDetectionTimer);
            
            const button = document.querySelector('button');
            const userMessage = document.getElementById("userMessage").value.trim();
            
            if (!userMessage) return;

            button.disabled = true;
            button.innerHTML = 'Sending...';
            
            addMessageToHistory(userMessage, true);
            
            try {
                const response = await fetch("/chat", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ 
                        message: userMessage,
                        type: "regular"
                    })
                });

                if (response.ok) {
                    const data = await response.json();
                    const botResponse = data.message?.content || "No response content";
                    addMessageToHistory(botResponse, false);
                    if (autoSpeak) {
                        speakMessage(botResponse);
                    }
                    document.getElementById("userMessage").value = '';
                } else {
                    addMessageToHistory("Error: Unable to get response", false);
                }
            } catch (error) {
                addMessageToHistory(`Error: ${error.message}`, false);
            } finally {
                button.disabled = false;
                button.innerHTML = 'Send';
                resetInactivityTimer();
            }
        }

        function formatTime() {
            const now = new Date();
            return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        }

        function addMessageToHistory(message, isUser) {
            const chatHistory = document.getElementById('chatHistory');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
            
            const messageContent = document.createElement('div');
            messageContent.className = 'message-content';
            messageContent.textContent = message;
            
            const timeDiv = document.createElement('div');
            timeDiv.className = 'message-time';
            timeDiv.textContent = formatTime();
            
            if (!isUser) {
                const speakButton = document.createElement('button');
                speakButton.className = 'speak-button';
                speakButton.innerHTML = '🔊';
                speakButton.onclick = () => speakMessage(message);
                messageDiv.appendChild(speakButton);
            }
            
            messageDiv.appendChild(messageContent);
            messageDiv.appendChild(timeDiv);
            chatHistory.appendChild(messageDiv);
            
            if (!isUser) {
                speakMessage(message);
            }
            
            chatHistory.scrollTop = chatHistory.scrollHeight;
        }

        async function fetchCurrentEmotion() {
            try {
                const response = await fetch("/current_emotion");
                const data = await response.json();
                document.getElementById("emotionText").innerText = data.emotion;
            } catch (error) {
                console.error("Error fetching current emotion:", error);
                document.getElementById("emotionText").innerText = "Error";
            }
        }

        async function fetchCurrentObjects() {
            try {
                const response = await fetch("/current_objects");
                const data = await response.json();
                document.getElementById("obj1Text").innerText = data.obj1;
                document.getElementById("obj2Text").innerText = data.obj2;
                document.getElementById("obj3Text").innerText = data.obj3;
            } catch (error) {
                console.error("Error fetching detected objects:", error);
                document.getElementById("obj1Text").innerText = "Error";
                document.getElementById("obj2Text").innerText = "Error";
                document.getElementById("obj3Text").innerText = "Error";
            }
        }

        setInterval(fetchCurrentEmotion, 2000);
        setInterval(fetchCurrentObjects, 2000);
        fetchCurrentEmotion();
        fetchCurrentObjects();

        // Add enter key support for sending messages
        document.getElementById("userMessage").addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                event.preventDefault();
                sendMessage();
            }
        });

        document.addEventListener('DOMContentLoaded', async () => {
            await initVoices();
            resetInactivityTimer();
            
            document.getElementById("userMessage").addEventListener('keypress', function() {
                resetInactivityTimer();
            });
        });

        let autoSpeak = true;

        function toggleAudio() {
            autoSpeak = !autoSpeak;
            const audioToggle = document.getElementById('audioToggle');
            audioToggle.innerHTML = autoSpeak ? '🔊' : '🔇';
            
            if (!autoSpeak && speaking) {
                speechSynthesis.cancel();
                speaking = false;
            }
        }

        async function checkPersonPresence() {
            try {
                const response = await fetch("/chat", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ 
                        message: "",
                        type: "person_check"
                    })
                });

                if (response.ok) {
                    const data = await response.json();
                    const botResponse = data.message?.content;
                    if (botResponse) {  // Only add message if someone disappeared
                        addMessageToHistory(botResponse, false);
                        if (autoSpeak) {
                            speakMessage(botResponse);
                        }
                    }
                }
            } catch (error) {
                console.error("Error checking person presence:", error);
            }
        }

        // Add cleanup when leaving the page
        window.addEventListener('beforeunload', () => {
            clearInterval(personCheckTimer);
        });

        let recognition;
        let isListening = false;

        function initializeSpeechRecognition() {
            if ('webkitSpeechRecognition' in window) {
                recognition = new webkitSpeechRecognition();
                recognition.continuous = false;
                recognition.interimResults = false;
                recognition.lang = 'en-US';

                recognition.onstart = function() {
                    isListening = true;
                    const voiceButton = document.getElementById('voiceButton');
                    const micIcon = document.getElementById('micIcon');
                    voiceButton.classList.add('recording');
                    micIcon.src = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNkYzM1NDUiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTIgMXY2di02Wm00IDZhNCA0IDAgMCAxLTggMFY3YTQgNCAwIDEgMSA4IDB2NVoiLz48cGF0aCBkPSJNMTkgMTB2MmE3IDcgMCAwIDEtMTQgMHYtMk0xMiAxOHY0di00Wm0wIDRoNGgtNFptMCAwaC00aDRaIi8+PC9zdmc+";
                };

                recognition.onend = function() {
                    isListening = false;
                    const voiceButton = document.getElementById('voiceButton');
                    const micIcon = document.getElementById('micIcon');
                    voiceButton.classList.remove('recording');
                    micIcon.src = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMiAxdjZ2LTZabTQgNmE0IDQgMCAwIDEtOCAwVjdhNCA0IDAgMSAxIDggMHY1WiIvPjxwYXRoIGQ9Ik0xOSAxMHYyYTcgNyAwIDAgMS0xNCAwdi0yTTEyIDE4djR2LTRabTAgNGg0aC00Wm0wIDBoLTRoNFoiLz48L3N2Zz4=";
                };

                recognition.onresult = function(event) {
                    const transcript = event.results[0][0].transcript;
                    document.getElementById('userMessage').value = transcript;
                    // Automatically send message after voice input
                    sendMessage();
                };

                recognition.onerror = function(event) {
                    console.error('Speech recognition error:', event.error);
                    isListening = false;
                    const voiceButton = document.getElementById('voiceButton');
                    const micIcon = document.getElementById('micIcon');
                    voiceButton.classList.remove('recording');
                    micIcon.src = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMiAxdjZ2LTZabTQgNmE0IDQgMCAwIDEtOCAwVjdhNCA0IDAgMSAxIDggMHY1WiIvPjxwYXRoIGQ9Ik0xOSAxMHYyYTcgNyAwIDAgMS0xNCAwdi0yTTEyIDE4djR2LTRabTAgNGg0aC00Wm0wIDBoLTRoNFoiLz48L3N2Zz4=";
                };
            } else {
                console.error('Speech recognition not supported in this browser');
            }
        }

        function startVoiceInput() {
            if (!recognition) {
                initializeSpeechRecognition();
            }

            if (isListening) {
                recognition.stop();
            } else {
                recognition.start();
            }
        }

        // Initialize speech recognition when the page loads
        document.addEventListener('DOMContentLoaded', function() {
            initializeSpeechRecognition();
            // ... your existing DOMContentLoaded code ...
        });

        // Add keyboard shortcut for voice input (Space key)
        document.addEventListener('keydown', function(event) {
            // Only trigger if not in text input and space is pressed
            if (event.code === 'Space' && document.activeElement.tagName !== 'INPUT') {
                event.preventDefault();
                startVoiceInput();
            }
        });
    </script>
</body>
</html>
