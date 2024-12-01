from flask import Flask, render_template
from flask_socketio import SocketIO
from knee_data import get_knee_data

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

@app.route('/')
def home():
    return render_template("dashboard.html", pages=pages, exercises=exercises)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', pages=pages, exercises=exercises)

@app.route('/measure_recovery')
def recovery_time():
    return render_template('recovery_time.html', pages=pages, exercises=exercises)

@app.route('/sensor_data')
def sensor_data():
    return render_template('sensor_data.html', pages=pages, exercises=exercises)

@app.route('/sit_to_stand')
def sit_to_stand():
    return render_template('exer_sit_to_stand.html', pages=pages, exercises=exercises)

@app.route('/assisted_walking')
def assisted_walking():
    return render_template('exer_assisted_walking.html', pages=pages, exercises=exercises)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('start_data_stream')
def stream_knee_data():
    while True:
        # try to catch exception in knee_data
        try:
            data = get_knee_data()
            if data:
                socketio.emit('knee_data', data)
            else:
                socketio.emit('knee_data', {"error": "No data available"})
                print("No data to emit")
        except Exception as e:
            print(f"Error in stream_knee_data: {e}")
            socketio.emit('knee_data', {"error": f"Error: {str(e)}"})
        socketio.sleep(0.1)

if __name__ == "__main__":
    billy_host = '192.168.221.24'  # host=billy_host
    eye_foam = '172.20.10.7'  # host=eye_foam
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True, host='0.0.0.0')  # allow_unsafe_werkzeug=True to run on Thonny shell