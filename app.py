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