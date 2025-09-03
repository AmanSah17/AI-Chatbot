import { useState } from "react";
import { apiRequest } from "../api";

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const token = localStorage.getItem("token");

  const sendMessage = async () => {
    if (!input.trim()) return;
    setMessages([...messages, { sender: "user", text: input }]);

    try {
      const response = await apiRequest("/chat", "POST", { message: input }, token);
      setMessages((prev) => [...prev, { sender: "bot", text: response.reply }]);
    } catch (err) {
      setMessages((prev) => [...prev, { sender: "bot", text: "Error: " + err.message }]);
    }
    setInput("");
  };

  return (
    <div className="chat-container">
      <h2>AI Chatbot</h2>
      <div className="chat-box">
        {messages.map((msg, idx) => (
          <p key={idx} className={msg.sender}>{msg.sender}: {msg.text}</p>
        ))}
      </div>
      <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Type a message..." />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default Chatbot;
