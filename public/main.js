document.addEventListener("DOMContentLoaded", () => {
    var socket = io();
    var messages = document.getElementById('messages');
    var typingIndicator = document.getElementById('typingIndicator');
    var input = document.getElementById('input');
    var sendButton = document.getElementById('send');
    
    var typingTimeout; // Variable to hold timeout ID for typing message
    
    
    function addMessage(message, sender) {
        var item = document.createElement('div');
        item.classList.add('message', sender);
        

        if (sender === 'chatbot') {
            var img = document.createElement('img');
            img.src = "./images/3.avif"; // icon for the bot in every message
            img.alt = 'bot icon';
            img.classList.add('message-icon'); // name used for its css 
            
            // we append it here to the item
            item.appendChild(img);
        }
        if (sender === 'user') {
            // follow the same process for the user!! 
            var img = document.createElement('img');
            img.src = "./images/user-icon.jpg"; 
            img.alt = 'user icon';
            img.classList.add('user-icon'); 
            
            
            item.appendChild(img);
        }
        var textNode = document.createElement('span');
        textNode.innerHTML = message;
        item.appendChild(textNode);

    
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
            adjustTextareaHeight(); 
        }
    };
    
    input.addEventListener('keypress', function(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault(); // Prevent adding a new line
            sendButton.click();
        }
    });
    
    input.addEventListener('input', function() {
        clearTimeout(typingTimeout); 
        showTypingIndicator(); // Show that the user is typing
    
        // we set 1 second for hiding the typing indicator
        typingTimeout = setTimeout(function() {
            hideTypingIndicator();
        }, 1000);
    });
    
    function showTypingIndicator() {
        typingIndicator.textContent = 'User is typing...'; // this message will be displayed when the user is writing something!!
    }
    
    function hideTypingIndicator() {
        typingIndicator.textContent = '';
    }
    
    function adjustTextareaHeight() {
        input.style.height = 'auto';
        input.style.height = (input.scrollHeight) + 'px';
    }
    
});
