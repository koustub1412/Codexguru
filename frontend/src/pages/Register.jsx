import React, { useState } from "react";
import axios from "axios";

function Register() {
  const [form, setForm] = useState({ username: "", email: "", password: "" });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleRegister = async () => {
    try {
      await axios.post(`${process.env.REACT_APP_API_BASE_URL}/register`, form);
      alert("Registered successfully!");
      window.location.href = "/login";
    } catch (err) {
      alert("Registration failed.");
    }
  };

  return (
    <div className="h-screen w-screen flex justify-center items-center bg-gradient-to-b from-gray-100 to-blue-100">
      <div className="w-full max-w-md bg-white p-8 rounded-xl shadow-xl flex flex-col space-y-4 items-center">
        <h2 className="text-3xl font-bold text-indigo-700">Register</h2>
        <input
          name="username"
          placeholder="Username"
          className="w-full p-3 border border-gray-300 rounded-md"
          onChange={handleChange}
        />
        <input
          name="email"
          placeholder="Email"
          className="w-full p-3 border border-gray-300 rounded-md"
          onChange={handleChange}
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          className="w-full p-3 border border-gray-300 rounded-md"
          onChange={handleChange}
        />
        <button
          onClick={handleRegister}
          className="w-full bg-indigo-600 hover:bg-indigo-700 text-white py-2 rounded-md"
        >
          Register
        </button>
      </div>
    </div>
  );
}

export default Register;
