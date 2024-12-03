from flask import Flask, render_template
from flask_socketio import SocketIO
import joblib
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Load the trained model using joblib
model_path = "rfr_model.sav"
random_forest_model = joblib.load(model_path)

@socketio.on('request_prediction')
def handle_prediction_request(data):
    try:
        # Retrieve the knee angle from the request data
        max_knee_angle = data.get('knee_angle', 0)
        
        # Preprocess the data (convert to a 2D array as required by scikit-learn models)
        features = np.array([[max_knee_angle]])
        
        # Perform prediction
        predicted_weeks = random_forest_model.predict(features)[0]
        
        # Send the prediction result back to the client
        socketio.emit('knee_data', {
            'knee_angle': max_knee_angle,
            'predicted_recovery_time': predicted_weeks
        })
    except Exception as e:
        # Handle any errors and send back an error message
        socketio.emit('knee_data', {'error': str(e)})

if __name__ == '__main__':
    socketio.run(app, debug=True)
