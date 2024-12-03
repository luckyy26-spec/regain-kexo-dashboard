// Initialize WebSocket connection
const socket = io();

// Register callbacks for live data
let liveDataCallbacks = [];

// Function to register a callback
function registerLiveDataCallback(callback) {
  liveDataCallbacks.push(callback);
}

// Emit start signal when connected
socket.on('connect', () => {
  console.log('Connected to server');
  socket.emit('start_data_stream');
});

// Handle incoming data and notify registered callbacks
socket.on('knee_data', (data) => {
  if (data) {
    console.log('Received data:', data);
    liveDataCallbacks.forEach((callback) => callback(data));
  }
});