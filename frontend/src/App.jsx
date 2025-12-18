import { useState } from "react";

export default function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message.trim()) {
      alert("Please enter a message");
      return;
    }

    console.log("👉 Sending message:", message);
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
      });

      console.log("👉 HTTP status:", res.status);

      const data = await res.json();
      console.log("👉 Backend response:", data);

      setResponse(data.response);
    } catch (error) {
      console.error("❌ Fetch error:", error);
      setResponse("Error connecting to backend");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>🌦️ Weather AI Assistant</h1>

      <input
        placeholder="Ask weather of any city..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && sendMessage()}
      />

      <button onClick={sendMessage} disabled={loading}>
        {loading ? "Thinking..." : "Send"}
      </button>

      {response && <div className="response">{response}</div>}
    </div>
  );
}
