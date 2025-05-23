import { useState } from "react";

export default function Home() {
  const [lead, setLead] = useState("");
  const [status, setStatus] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus("Processing...");
    try {
      const res = await fetch("/api/callAgent", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ lead }),
      });
      const data = await res.json();
      if (res.ok) {
        setStatus("Call initiated successfully!");
      } else {
        setStatus(`Error: ${data.error}`);
      }
    } catch (err) {
      setStatus(`Error: ${err.message}`);
    }
  };

  return (
    <div style={{ padding: "20px", textAlign: "center" }}>
      <h1>LeadReviveAI</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter lead phone number"
          value={lead}
          onChange={(e) => setLead(e.target.value)}
          required
          style={{ padding: "10px", marginBottom: "10px", width: "300px" }}
        />
        <br />
        <button type="submit" style={{ padding: "10px 20px" }}>
          Initiate Call
        </button>
      </form>
      <p>{status}</p>
    </div>
  );
}
