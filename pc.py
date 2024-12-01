from flask import Flask, render_template

app = Flask(__name__, 
            template_folder='pages', 
            static_folder='assets',
            static_url_path='/assets'
            )

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

if __name__ == "__main__":
    app.run(debug=True) 