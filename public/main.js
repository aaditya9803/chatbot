import { io } from "https://cdn.socket.io/4.7.5/socket.io.esm.min.js";

document.addEventListener("DOMContentLoaded", () => {
  const socket = io(); // Connect to the current host

  const btn = document.querySelector(".conserve");
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");

  const sendMessage = () => {
    const questionUSER = input.value.trim();
    if (questionUSER !== "") {
      // Emit user's question to the server
      socket.emit("request", questionUSER);

      // Display user's question in the chat box
      const questionDiv = document.createElement("div");
      questionDiv.classList.add("message", "user");
      questionDiv.textContent = questionUSER;
      chatBox.appendChild(questionDiv);

      // Clear the input field
      input.value = "";
      input.style.height = "40px"; // Reset height after sending message

      // Scroll to the bottom of the chat box
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  };

  btn.addEventListener("click", sendMessage);

  socket.on("response", (data) => {
    // Display server's response in the chat box
    const answerDiv = document.createElement("div");
    answerDiv.classList.add("message", "bot");
    answerDiv.textContent = data;
    chatBox.appendChild(answerDiv);

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
  });

  // Adjust the height of the textarea as the user types
  input.addEventListener("input", function() {
    this.style.height = "auto";
    this.style.height = (this.scrollHeight) + "px";
  });

  // Handle enter and shift+enter for sending message and new line
  input.addEventListener("keydown", function(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });
});