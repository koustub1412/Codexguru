import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard"; // <- make sure this exists

function App() {
return (
<Router>
<Routes>
<Route path="/" element={<Login />} />
<Route path="/register" element={<Register />} />
<Route path="/dashboard" element={<Dashboard />} /> {/* this line is needed */}
</Routes>
</Router>
);
}

export default App;