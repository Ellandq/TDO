const express = require("express");
const axios = require("axios");
const path = require("path");

const app = express();
const PORT = 3000;

app.use(express.static(path.join(__dirname, "public")));

app.get("/ping", async (req, res) => {
  try {
    const response = await axios.get("http://backend:5000/users");
    res.json({ ok: true, users: response.data });
  } catch (err) {
    console.error("Error forwarding to backend:", err.message);
    res.status(500).json({ error: "Backend request failed" });
  }
});

app.listen(PORT, () => {
  console.log(`Frontend proxy listening at http://localhost:${PORT}`);
});
