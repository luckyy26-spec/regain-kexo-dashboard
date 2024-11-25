from flask import Flask, render_template
# from flask_socketio import SocketIO
# from knee_data import get_knee_data

app = Flask(__name__, 
            template_folder='pages', 
            static_folder='assets',
            static_url_path='/assets'
            )

# socketio = SocketIO(app)

pages = [{
        "page_url": "dashboard",
        "page_icon": "dashboard",
        "page_name": "Dashboard"
    },{
        "page_url": "recovery_time",
        "page_icon": "view_in_ar",
        "page_name": "Recovery Time"
    }]

exercises = [{
        "page_url": "aerobic_activity",
        "page_icon": "receipt_long",
        "page_name": "Aerobic Activity"
    },{
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
'''
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
    billy_host = '192.168.221.24' # host=billy_host
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True) # allow_unsafe_werkzeug=True in order to run on thonny shell
'''

