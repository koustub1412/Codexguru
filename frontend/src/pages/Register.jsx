
// Register.jsx
import React, { useState } from "react";
import { TextField, Button, Typography, Container, Paper } from "@mui/material";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Register() {
  const [form, setForm] = useState({ username: "", email: "", password: "" });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleRegister = async () => {
    try {
      await axios.post(`${process.env.REACT_APP_API_BASE_URL}/register`, form, {
        headers: { "Content-Type": "application/json" },
      });
      alert("Registered successfully! Please log in.");
      navigate("/login");
    } catch (err) {
      alert("Registration failed.");
    }
  };

  return (
    <Container maxWidth="xs" style={{ marginTop: 80 }}>
      <Paper style={{ padding: 30, backgroundColor: "#1E1E1E" }}>
        <Typography variant="h5" gutterBottom style={{ color: "#ffffff" }}>
          Register
          
        </Typography>
        <TextField
          fullWidth
          label="Username"
          name="username"
          value={form.username}
          onChange={handleChange}
          margin="normal"
          InputLabelProps={{ style: { color: "#e0e0e0" } }}
          InputProps={{ style: { color: "#ffffff" } }}
        />
        <TextField
          fullWidth
          label="Email"
          type="email"
          name="email"
          value={form.email}
          onChange={handleChange}
          margin="normal"
          InputLabelProps={{ style: { color: "#e0e0e0" } }}
          InputProps={{ style: { color: "#ffffff" } }}
        />
        <TextField
          fullWidth
          label="Password"
          type="password"
          name="password"
          value={form.password}
          onChange={handleChange}
          margin="normal"
          InputLabelProps={{ style: { color: "#e0e0e0" } }}
          InputProps={{ style: { color: "#ffffff" } }}
        />
        <Button fullWidth variant="contained" color="primary" onClick={handleRegister} style={{ marginTop: 20 }}>
          Register
        </Button>
      </Paper>
    </Container>
  );
}

export default Register;