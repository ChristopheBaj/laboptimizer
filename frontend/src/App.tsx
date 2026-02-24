import { useState } from "react";
import "./App.css";

export default function App() {
  const [msg, setMsg] = useState<string>("");

  return (
    <div style={{ padding: 24, fontFamily: "system-ui, sans-serif" }}>
      <h1>LabOptimizer</h1>
      <p>Minimal UI prototype (React + TypeScript)</p>

      <button
        onClick={() => setMsg("Hello World !")}
        style={{
          padding: "10px 14px",
          borderRadius: 8,
          border: "10px solid #4218b3",
          cursor: "pointer",
        }}
      >
        Click me
      </button>

      {msg && (
        <div style={{ marginTop: 16, padding: 12, border: "1px solid #eee" }}>
          <strong>Message:</strong> {msg}
        </div>
      )}
    </div>
  );
}
