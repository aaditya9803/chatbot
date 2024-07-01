document.addEventListener("DOMContentLoaded", () => {
    const socket = io();

    const messages = document.getElementById('messages');
    const input = document.getElementById('input');
    const sendButton = document.getElementById('send');

    function addMessage(message, sender) {
        const item = document.createElement('div');
        item.classList.add('message', sender);
        item.innerHTML = message;
        messages.appendChild(item);
        messages.scrollTop = messages.scrollHeight;
    }

    socket.on('chatbot message', (msg) => {
        addMessage(msg, 'chatbot');
    });

    sendButton.onclick = () => {
        const msg = input.value.trim();
        if (msg) {
            addMessage(msg, 'user');
            socket.emit('user message', msg);
            input.value = '';
            adjustTextareaHeight();
        }
    };

    input.addEventListener('keypress', (event) => {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            sendButton.click();
        }
    });

    function adjustTextareaHeight() {
        input.style.height = 'auto';
        input.style.height = (input.scrollHeight) + 'px';
    }

    input.addEventListener('input', adjustTextareaHeight);
});