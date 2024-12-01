from flask import Flask, render_template
from flask_socketio import SocketIO
from knee_data import get_knee_data
from flask_socketio import SocketIO, emit
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import os

app = Flask(__name__,
            template_folder='pages',
            static_folder='assets',
            static_url_path='/assets')

socketio = SocketIO(app)

pages = [{
        "page_url": "dashboard",
        "page_icon": "dashboard",
        "page_name": "Dashboard"
    },{
        "page_url": "sensor_data",
        "page_icon": "sensors",
        "page_name": "Sensor Data"
    },{
        "page_url": "recovery_time",
        "page_icon": "view_in_ar",
        "page_name": "Recovery Time"
    }]

exercises = [{
        "page_url": "assisted_walking",
        "page_icon": "receipt_long",
        "page_name": "Assisted Walking"
    },{
        "page_url": "sit_to_stand",
        "page_icon": "balance",
        "page_name": "Sit to Stand"
    }]

# Function to train model
def train_model():
    data = pd.read_csv('regression_data.csv')
    data = data.dropna().drop_duplicates()

    # Prepare data
    X = data[['Max_knee_flexion']]
    y = data['Estimated_recovery_time_week']

    # Train model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor.fit(X_train, y_train)
    return rf_regressor


# Initialize model
rf_model = train_model()


# Function to handle real-time data processing
def process_real_time_data(knee_angle):
    # Predict for given knee angle
    predicted_recovery_time = rf_model.predict([[knee_angle]])

    # Generate visualization
    plt.figure(figsize=(8, 6))
    plt.scatter(rf_model.feature_importances_, rf_model.oob_score_, alpha=0.7, color='blue')
    plt.axvline(x=knee_angle, color='red', linestyle='--', label=f'Input Knee Angle: {knee_angle}')
    plt.title('Max Knee Flexion vs Recovery Time')
    plt.xlabel('Max Knee Flexion (degrees)')
    plt.ylabel('Recovery Time (weeks)')
    plt.legend()
    plt.grid(True)

    # Save plot to static folder
    plot_path = os.path.join(app.static_folder, 'images', 'real_time_visualization.png')
    os.makedirs(os.path.dirname(plot_path), exist_ok=True)
    plt.savefig(plot_path)
    plt.close()

    return round(predicted_recovery_time[0], 2), '/assets/img/real_time_visualization.png'


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
def start_data_stream():
    try:
        for knee_angle in range(60, 91, 5):  # Simulate real-time knee angle data
            predicted_time, plot_path = process_real_time_data(knee_angle)

            # Emit data to frontend
            socketio.emit('recovery_prediction', {
                'knee_angle': knee_angle,
                'predicted_time': predicted_time,
                'plot_path': plot_path
            })

            socketio.sleep(1)  # Simulate a delay for real-time processing

    except Exception as e:
        print(f"Error in data stream: {e}")
        socketio.emit('recovery_prediction', {"error": f"Error: {str(e)}"})


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
