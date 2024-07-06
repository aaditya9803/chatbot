const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const { exec } = require('child_process');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.use(express.static('public'));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

let userStates = {};

io.on('connection', (socket) => {
    console.log('a user connected');

    userStates[socket.id] = { lastMessage: null };

    socket.emit('chatbot message', 'Welcome to our DIT canteen <br> I\'m PRINI the bot <br>');

    socket.on('user message', (msg) => {
        console.log('message from user: ' + msg);

        const userState = JSON.stringify(userStates[socket.id]);
        exec(`python3 chatbot.py "${msg.replace(/"/g, '\\"')}" "${userState.replace(/"/g, '\\"')}"`, (error, stdout, stderr) => {
            if (error) {
                console.error(`exec error: ${error}`);
                return;
            }

            const response = JSON.parse(stdout.trim());
            userStates[socket.id] = response.state;
            socket.emit('chatbot message', response.message);
        });
    });

    socket.on('disconnect', () => {
        console.log('user disconnected');
        delete userStates[socket.id];
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`listening on *:${PORT}`);
});
