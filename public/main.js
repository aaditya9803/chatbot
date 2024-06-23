var socket = io();
        var messages = document.getElementById('messages');
        var input = document.getElementById('input');
        var sendButton = document.getElementById('send');

        function addMessage(message, sender) {
            var item = document.createElement('div');
            item.textContent = message;
            item.classList.add(sender);
            messages.appendChild(item);
            messages.scrollTop = messages.scrollHeight;
        }
 
        socket.on('chatbot message', function(msg) {
            addMessage(msg, 'chatbot');
        });

        sendButton.onclick = function() {
            var msg = input.value;
            if (msg) {
                addMessage(msg, 'user');
                socket.emit('user message', msg);
                input.value = '';
            }
        };

        input.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                sendButton.click();
            }
        });