import { useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function App() {
  const [code, setCode] = useState("");
  const [summary, setSummary] = useState("");
  const [debugResult, setDebugResult] = useState("");
  const [error, setError] = useState("");

  const handleAnalyze = async () => {
    const token = localStorage.getItem("token");
    if (!token) {
      alert("User not authenticated. Please log in.");
      return;
    }

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/analyze",
        { code },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setSummary(res.data.summary);
    } catch (err) {
      console.error("Analyze error:", err);
      alert("Analysis failed.");
    }
  };

  const handleDebug = async () => {
    const token = localStorage.getItem("token");

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/debug",
        { code },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setDebugResult(res.data.output);
    } catch (err) {
      alert("Debugging failed.");
    }
  };
return (
  <div className="h-full w-full bg-gradient-to-b from-gray-100 to-blue-100 flex justify-center items-center">
    <div className="w-full max-w-3xl bg-white shadow-2xl rounded-xl p-8 flex flex-col items-center space-y-6">

      <div className="flex flex-col items-center space-y-2">
        <h1 className="text-4xl font-bold text-indigo-700">CodexGuru</h1>
        <div className="space-x-4">
          <Link to="/login">
            <button className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-md shadow">Login</button>
          </Link>
          <Link to="/register">
            <button className="bg-yellow-500 hover:bg-yellow-600 text-white px-4 py-2 rounded-md shadow">Register</button>
          </Link>
        </div>
      </div>

      <textarea
        rows={10}
        className="w-full p-4 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-400 resize-none"
        placeholder="Paste your code here..."
        value={code}
        onChange={(e) => setCode(e.target.value)}
      />

      <div className="flex justify-center gap-4">
        <button
          onClick={handleAnalyze}
          className="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-2 rounded-md shadow"
        >
          🧪 Analyze
        </button>
        <button
          onClick={handleDebug}
          className="bg-red-600 hover:bg-red-700 text-white px-6 py-2 rounded-md shadow"
        >
          🐞 Debug
        </button>
      </div>

      {summary && (
        <div className="w-full bg-pink-50 border border-pink-300 rounded-md p-4 max-h-60 overflow-y-auto">
          <h2 className="text-lg font-semibold text-pink-800 mb-2">🧠 Code Summary</h2>
          <pre className="text-sm text-gray-800 whitespace-pre-wrap">{summary}</pre>
        </div>
      )}

      {debugResult && (
        <div className="w-full bg-blue-50 border border-blue-300 rounded-md p-4 max-h-60 overflow-y-auto">
          <h2 className="text-lg font-semibold text-blue-800 mb-2">🔍 Debugging Result</h2>
          <pre className="text-sm text-gray-900 whitespace-pre-wrap">{debugResult}</pre>
        </div>
      )}
    </div>
  </div>
);

}

export default App;
