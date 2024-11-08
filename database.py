from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint to receive sensor data
@app.route('/sensor-data', methods=['GET'])
def get_sensor_data():
    # Placeholder for sensor data; replace this with actual data from the sensor
    sensor_data = {
        "accelerometer": {
            "x": 0.0,
            "y": 0.0,
            "z": 0.0
        },
        "gyroscope": {
            "x": 0.0,
            "y": 0.0,
            "z": 0.0
        }
    }
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(debug=True)
