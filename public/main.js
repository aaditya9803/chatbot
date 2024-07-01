var socket = io();
var messages = document.getElementById('messages');
var input = document.getElementById('input');
var sendButton = document.getElementById('send');

function addMessage(message, sender) {
    var item = document.createElement('div');
    item.classList.add('message', sender);
    item.textContent = message;
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
        adjustTextareaHeight(); // Reset the height after sending
    }
};

input.addEventListener('keypress', function(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault(); // Prevent adding a new line
        sendButton.click();
    }
});

function adjustTextareaHeight() {
    input.style.height = 'auto';
    input.style.height = (input.scrollHeight) + 'px';
}

input.addEventListener('input', adjustTextareaHeight);
