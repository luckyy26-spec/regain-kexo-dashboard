from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Flask app setup
app = Flask(
    __name__,
    template_folder='pages',
    static_folder='assets',
    static_url_path='/assets'
)
socketio = SocketIO(app)

# Directory to save plots
PLOT_DIR = 'assets/plots'
os.makedirs(PLOT_DIR, exist_ok=True)

# Load and train the Random Forest model
data = pd.read_csv('regression_data.csv')
X = data[['Max_knee_flexion']]
y = data['Estimated_recovery_time_week']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train, y_train)

# Define pages
pages = [{
    "page_url": "dashboard",
    "page_icon": "dashboard",
    "page_name": "Dashboard"
}, {
    "page_url": "recovery_time",
    "page_icon": "view_in_ar",
    "page_name": "Recovery Time"
}]

exercises = [{
    "page_url": "aerobic_activity",
    "page_icon": "receipt_long",
    "page_name": "Aerobic Activity"
}, {
    "page_url": "balance_training",
    "page_icon": "balance",
    "page_name": "Balance Training"
}]

@app.route('/')
def home():
    return render_template("dashboard.html", pages=pages, exercises=exercises)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', pages=pages, exercises=exercises)

@app.route('/balance_training')
def balance_training():
    return render_template('balance_training.html', pages=pages, exercises=exercises)

@app.route('/aerobic_activity')
def aerobic_activity():
    return render_template('aerobic_activity.html', pages=pages, exercises=exercises)

@app.route('/measure_recovery')
def recovery_time():
    return render_template('recovery_time.html', pages=pages, exercises=exercises)

@socketio.on('start_data_stream')
def stream_knee_data():
    try:
        # Example knee angle data over time
        days = np.arange(1, 16) 
        knee_angles = np.array([60, 65, 70, 75, 80, 82, 85, 88, 90, 89, 87, 85, 83, 80, 78])

        # Predict recovery time based on the maximum knee angle
        max_knee_angle = knee_angles.max()
        predicted_recovery_time = rf_regressor.predict([[max_knee_angle]])[0]

        # Generate and save the plot
        plot_file = os.path.join(PLOT_DIR, 'knee_progress.png')
        plt.figure(figsize=(10, 6))
        plt.plot(days, knee_angles, marker='o', color='blue', label='Knee Angle')
        plt.axhline(y=max_knee_angle, color='red', linestyle='--', label=f'Max Knee Angle: {max_knee_angle}°')
        plt.title('Knee Angle Progress')
        plt.xlabel('Days')
        plt.ylabel('Knee Angle (degrees)')
        plt.legend()
        plt.grid(True)
        plt.savefig(plot_file)
        plt.close()

        # Emit the data including visualization URL
        socketio.emit('knee_data', {
            "max_knee_angle": max_knee_angle,
            "predicted_recovery_time": round(predicted_recovery_time, 2),
            "visualization_url": f'/assets/img/knee_progress.png'
        })
    except Exception as e:
        print(f"Error in stream_knee_data: {e}")
        socketio.emit('knee_data', {"error": str(e)})

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
    billy_host = '192.168.221.24'  # host=billy_host
    eye_foam = '172.20.10.7'  # host=eye_foam
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True, host='0.0.0.0')  # allow_unsafe_werkzeug=True to run on Thonny shell
