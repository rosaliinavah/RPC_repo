const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const fs = require("fs");

const app = express();
app.use(express.json());
app.use(cors());

// Start server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});

// Connect to MongoDB Atlas
mongoose.connect("mongodb+srv://rvahapesola_db:kayttajasalasana1@testcluster.yps41pp.mongodb.net/plcdata?retryWrites=true&w=majority")
  .then(() => console.log("MongoDB connected"))
  .catch(err => console.error("MongoDB error:", err));

// Mongoose schema
const plcSchema = new mongoose.Schema({
  pt100: Number,
  pt1000: Number,
  latitude: Number,
  longitude: Number,
  altitude: Number,
  timestamp: { type: Date, default: Date.now }
});

const PlcData = mongoose.model("PlcData", plcSchema);

// GET endpoint UI:lle
app.get("/api/plc/latest", (req, res) => {
  try {
    res.json(latestData);
  } catch (err) {
    console.error("Fetch error:", err);
    res.status(500).json({ error: err.message });
  }
});

// Test route
app.get("/", (req, res) => {
  res.send("Server is running");
});

// Read data.json and save data to MongoDB
const saveDataFromFile = async () => {
  try {
    const raw = fs.readFileSync("data.json", "utf-8");
    const jsonData = JSON.parse(raw);

    const data = new PlcData(jsonData);
    await data.save();

    console.log("Saved to MongoDB from data.json:", jsonData);
  } catch (err) {
    console.error("Error reading or saving data.json:", err.message);
  }
};

// Read data.json
const readDataFile = () => {
  try {
    if (!fs.existsSync("data.json")) return
    const raw = fs.readFileSync("data.json", "utf-8").trim()
    if (!raw) return
    const parsed = JSON.parse(raw)
    latestData = parsed

  } catch (err) {
    console.log("Waiting for valid JSON...")
  }
}

// Update UI-data in 1s interval
setInterval(readDataFile, 1000);

// Send data to MongoDB in 30s interval
setInterval(saveDataFromFile, 30000); // 30 000 ms = 30 s

let latestData = { message: "No data yet" };