// Chart instance for knee angles
let recoveryChart;

function initializeChart() {
  const ctx = document.getElementById('recoveryChart').getContext('2d');
  recoveryChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [], // X-axis (button clicks)
      datasets: [
        {
          label: 'Maximum Knee Flexion',
          tension: 0.4,
          borderWidth: 2,
          pointRadius: 3,
          pointBackgroundColor: '#ff6384',
          pointBorderColor: 'transparent',
          borderColor: '#ff6384',
          backgroundColor: 'transparent',
          fill: false,
          data: [], // Y-axis (knee angles)
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          title: {
            display: true,
            text: 'Days',
          },
        },
        y: {
          title: {
            display: true,
            text: 'Recovery Chart',
          },
        },
      },
    },
  });
}

// Initialize the chart on page load
document.addEventListener('DOMContentLoaded', initializeChart);
