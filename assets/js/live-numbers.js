// Function to update the live numbers
function updateLiveNumbers(data) {
  const kneeData = (name, value) => `
    <div class="col mb-4 knee-data-item">
      <div class="card">
          <div class="card-header card-footer p-4 ps-4">
              <div class="d-flex justify-content-between">
                  <div>
                      <p class="text-sm mb-0 text-capitalize">${name}</p>
                      <h4 class="mb-0">${value}</h4>
                  </div>
                  <div>
                      <i class="material-icons opacity-10">sensors</i>
                  </div>
              </div>
          </div>
      </div>  
    </div>`;

  const container = document.getElementById('knee_data_container');
  container.innerHTML = `
    ${kneeData('Thigh Angle', `${data.pitch_thigh}°`)}
    ${kneeData('Knee Angle', `${data.knee_angle}°`)}
    ${kneeData('Shin Angle', `${data.pitch_shin}°`)}
    ${kneeData('Gait Phase', `${data.gait_phase}`)}
  `;
}

// Register the update function with the shared WebSocket
registerLiveDataCallback(updateLiveNumbers);