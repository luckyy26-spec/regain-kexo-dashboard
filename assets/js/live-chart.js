function updateLiveChart(data) {
  kneeChart.data.labels.push(data.gait_phase);
  kneeChart.data.datasets[0].data.push(data.pitch_thigh);
  kneeChart.data.datasets[1].data.push(data.knee_angle);
  kneeChart.data.datasets[2].data.push(data.pitch_shin);

  if (kneeChart.data.labels.length > 10) {
    kneeChart.data.labels.shift();
    kneeChart.data.datasets.forEach(dataset => dataset.data.shift());
  }

  kneeChart.update();
}

// Register the update function with the shared WebSocket
registerLiveDataCallback(updateLiveChart);