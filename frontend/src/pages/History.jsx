import React, { useEffect, useState } from "react";
import {
  Container,
  Paper,
  Typography,
  Button,
  Box,
  Grid,
} from "@mui/material";
import axios from "axios";

function History() {
  const [history, setHistory] = useState([]);
  const token = localStorage.getItem("token");

  const fetchHistory = async () => {
    try {
      const res = await axios.get(`${process.env.REACT_APP_API_BASE_URL}/history`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setHistory(res.data);
    } catch (err) {
      console.error("Failed to fetch history", err);
    }
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  const handleDelete = async (id) => {
    if (!window.confirm("Are you sure you want to delete this analysis?")) return;

    try {
      await axios.delete(`${process.env.REACT_APP_API_BASE_URL}/history/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      alert("Deleted successfully");
      fetchHistory();
    } catch (err) {
      console.error("Delete failed", err);
      alert("Failed to delete analysis.");
    }
  };

  return (
    <Container maxWidth="md" style={{ marginTop: 30 }}>
      <Typography variant="h5" gutterBottom style={{ color: "#1E1E1E" }}>
        🕘 Past Analyses
      </Typography>

      {history.length === 0 ? (
        <Typography style={{ color: "#ffffff" }}>No history found.</Typography>
      ) : (
        <Grid container spacing={3}>
          {history.map((entry) => (
            <Grid item xs={12} key={entry._id}>
              <Paper style={{ padding: 20, backgroundColor: "#1E1E1E" }}>
                <Typography variant="body2" style={{ color: "#ffffff" }}>
                  <strong>🕓 Time:</strong> {new Date(entry.timestamp).toLocaleString()}
                </Typography>

                <Typography variant="body2" style={{ color: "#ffffff" }}>
                  <strong>📄 Code:</strong>
                </Typography>
                <Box
                  component="pre"
                  sx={{ whiteSpace: "pre-wrap", fontFamily: "monospace" }}
                  style={{ color: "#ffffff" }}
                >
                  {entry.code}
                </Box>

                <Typography variant="body2" style={{ color: "#ffffff" }}>
                  <strong>📝 Summary:</strong>
                </Typography>
                <Box
                  component="pre"
                  sx={{ whiteSpace: "pre-wrap", fontFamily: "monospace" }}
                  style={{ color: "#ffffff" }}
                >
                  {entry.summary}
                </Box>

                <Typography variant="body2" style={{ color: "#ffffff" }}>
                  <strong>🐞 Debug:</strong>
                </Typography>
                <Box
                  component="pre"
                  sx={{ whiteSpace: "pre-wrap", fontFamily: "monospace" }}
                  style={{ color: "#ffffff" }}
                >
                  {entry.debug}
                </Box>

                <Button
                  variant="contained"
                  color="error"
                  onClick={() => handleDelete(entry._id)}
                  style={{ marginTop: 10 }}
                >
                  Delete
                </Button>
              </Paper>
            </Grid>
          ))}
        </Grid>
      )}
    </Container>
  );
}

export default History;
