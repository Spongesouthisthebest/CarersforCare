from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about-us")
def about():
    return render_template("about_us.html")

@app.route('/contact-us')
def contact():
    return render_template("contact.html")

@app.route('/ndis')
def ndis():
    return render_template("ndis.html")

@app.route('/assist-personal-activity')
def assist1():
    return render_template('s2.html')

@app.route('/assist-travel-transport')
def assist2():
    return render_template('s3.html')

@app.route('/community-participation')
def assist3():
    return render_template("s4.html")

@app.route('/daily-task-shared-living')
def assist5():
    return render_template("s6.html")

@app.route('/respite-care')
def assist6():
    return render_template("s7.html")

@app.route('/ndis-cleaning')
def assist7():
    return render_template('s8.html')

@app.route('/gardening')
def assist8():
    return render_template('s9.html')

@app.route('/sil')
def assist9():
    return render_template('s10.html')

@app.route('/assist-life-stage')
def assistance():
    return render_template('s5.html')
