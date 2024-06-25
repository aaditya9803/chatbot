var socket = io();
        var messages = document.getElementById('messages');
        var input = document.getElementById('input');
        var sendButton = document.getElementById('send');


        function addMessage(message, sender) {
            var item = document.createElement('div');
            item.style.marginBottom = "10px";
            item.textContent = message;
            item.style.backgroundColor = "#05cee9";
            item.style.color ="black";
            item.style.padding ="5px";
            item.style.borderRadius = "5px";
            item.style.marginLeft = "345px";
            item.style.textAlign ="right";
            item.style.fontSize = "15px"
            item.classList.add("message",sender);
            messages.appendChild(item);
            
            
            messages.scrollTop = messages.scrollHeight;
            
        }
        function addMessage1(message, sender) {
            var item2 = document.createElement('div');
            
            item2.textContent = message;
            item2.style.backgroundColor = "#584fd9";
            item2.style.marginBottom = "10px";
            item2.style.width = "350px";
            item2.style.padding ="5px";
            item2.style.borderRadius = "5px";
            item2.classList.add("message",sender);
            messages.appendChild(item2);
            messages.scrollTop = messages.scrollHeight;
            
        }


     

        
 
        socket.on('chatbot message', function(msg) {
            addMessage1(msg, 'chatbot');
        
        });

        sendButton.onclick = function() {
            var msg = input.value ;
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