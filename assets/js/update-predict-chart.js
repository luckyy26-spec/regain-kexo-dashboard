// Arrays to store chart data
const kneeAngles = [];
let clickCount = 0;

// Function to update the knee angle chart
function updateKneeAngleChart(kneeAngle) {
  clickCount++; // Increment button click count
  kneeAngles.push(kneeAngle); // Add the new knee angle

  // Update the chart
  kneeAngleChart.data.labels.push(clickCount); // X-axis
  kneeAngleChart.data.datasets[0].data.push(kneeAngle); // Y-axis

  // Limit to last 10 points for better readability
  if (kneeAngles.length > 10) {
    kneeAngles.shift();
    kneeAngleChart.data.labels.shift();
    kneeAngleChart.data.datasets[0].data.shift();
  }

  kneeAngleChart.update();
}