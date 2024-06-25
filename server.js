const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

const PORT = process.env.PORT || 3000;

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

io.on('connection', (socket) => {
    console.log('a user connected');
    socket.on('disconnect', () => {
        console.log('user disconnected');
    });

    socket.on('request', (questionUSER) => {
      let response = '';
      if (questionUSER.toLowerCase().includes('order status')) {
        response = "Your order status is processing.";
      } else if (questionUSER.toLowerCase().includes('shipping')) {
        response = "Shipping usually takes 3-5 business days.";
      } else {
        response = "I'm sorry, I didn't understand that. How can I assist you?";
      }
      socket.emit('response', response);
    });
    
});

server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});