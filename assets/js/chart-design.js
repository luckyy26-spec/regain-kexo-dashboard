// Initialize the chart
const ctx = document.getElementById('chart-line').getContext('2d');
const kneeChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [], // Dynamic labels from socket data
    datasets: [
      {
        label: 'Thigh Angle',
        tension: 0.4,
        borderWidth: 2,
        pointRadius: 3,
        pointBackgroundColor: 'red',
        pointBorderColor: 'transparent',
        borderColor: 'red',
        backgroundColor: 'transparent',
        fill: true,
        data: [],
        maxBarThickness: 6,
      },
      {
        label: 'Knee Angle',
        tension: 0.4,
        borderWidth: 2,
        pointRadius: 3,
        pointBackgroundColor: 'blue',
        pointBorderColor: 'transparent',
        borderColor: 'blue',
        backgroundColor: 'transparent',
        fill: true,
        data: [],
        maxBarThickness: 6,
      },
      {
        label: 'Shin Angle',
        tension: 0.4,
        borderWidth: 2,
        pointRadius: 3,
        pointBackgroundColor: 'green',
        pointBorderColor: 'transparent',
        borderColor: 'green',
        backgroundColor: 'transparent',
        fill: true,
        data: [],
        maxBarThickness: 6,
      },

    ],
  },
  options: {
    responsive: false,
    maintainAspectRatio: false,
    animation: {
      duration: 0.1, // Smooth transitions
    },
    plugins: {
      legend: {
        display: true,
        position: 'bottom',
        align: 'end',
        boxWidth: 10

      },
      tooltip: {
        callbacks: {
          title: function (context) {
            return context[0].label; // Display dynamic labels
          },
        },
      },
    },
    interaction: {
      intersect: false,
      mode: 'index',
    },
    scales: {
      y: {
        title: {
            display: true,
            text: 'Angle (°)'
        },
        grid: {
          drawBorder: false,
          display: true,
          drawOnChartArea: true,
          drawTicks: false,
          borderDash: [4, 4],
          color: '#e5e5e5',
        },
        ticks: {
          display: true,
          color: '#737373',
          padding: 10,
          font: {
            size: 12,
            lineHeight: 2,
          },
        },
      },
      x: {
        title: {
            display: true,
            text: 'Gait Phase'
        },
        grid: {
          drawBorder: false,
          display: false,
          drawOnChartArea: false,
          drawTicks: false,
          borderDash: [5, 5],
        },
        ticks: {
          display: true,
          color: '#737373',
          padding: 10,
          font: {
            size: 12,
            lineHeight: 2,
          },
        },
      },
    },
  },
});