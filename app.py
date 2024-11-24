from flask import Flask, render_template

app = Flask(__name__, 
            template_folder='pages', 
            static_folder='assets',
            static_url_path='/assets'
            )

pages = [{
        "page_url": "dashboard",
        "age_icon": "dashboard",
        "page_name": "Dashboard"
    },
    {
        "page_url": "balance_training",
        "page_icon": "balance",
        "page_name": "Balance Training"
    },
    {
        "page_url": "aerobic",
        "page_icon": "receipt_long",
        "page_name": "Aerobic Activity"
    },
    {
        "page_url": "measure_recovery",
        "page_icon": "view_in_ar",
        "page_name": "Measure Recovery Time"
    }]

@app.route('/')
def home():
    return render_template("dashboard.html", page=pages)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', page=pages)

@app.route('/balance_training')
def balance_training():
    return render_template('balance_training.html', page=pages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)