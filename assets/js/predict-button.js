// Function to fetch the prediction from the backend
async function getPrediction(kneeAngle) {
    try {
      const response = await fetch('/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ knee_angle: kneeAngle }),
      });
  
      if (!response.ok) {
        throw new Error('Failed to fetch prediction');
      }
  
      const data = await response.json();
      if (data.error) {
        throw new Error(data.error);
      }
  
      return data.prediction;
    } catch (error) {
      console.error('Error fetching prediction:', error);
      return null;
    }
  }
  
  // Button click event
  document.getElementById('predictButton').addEventListener('click', async () => {
    const latestData = socket.latestData; // Retrieve the latest data from the shared WebSocket
    const kneeAngle = latestData?.knee_angle;
  
    if (kneeAngle !== undefined) {
      // Update the chart with the knee angle
      updateKneeAngleChart(kneeAngle);
  
      // Fetch the prediction
      const prediction = await getPrediction(kneeAngle);
  
      // Update the paragraph with the latest prediction
      if (prediction !== null) {
        document.getElementById('predictionParagraph').textContent = `Prediction: ${prediction}`;
      }
    } else {
      console.error('No valid knee angle data available.');
    }
  });
  