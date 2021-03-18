
#Question 1

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/home', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/calendar', methods=['GET'])
def calendar():
    return render_template("calendar.html")

@app.route('/coursecontent',methods=['GET'])
def coursecontent():
    return render_template("courseContent.html")

@app.route('/coursework',methods=["GET"])
def coursework():
    return render_template("coursework.html")

@app.route('/links',methods=["GET"])
def links():
    return render_template("links.html")

@app.route('/fun',methods=["GET"])
def fun():
    return render_template("links.html")


if __name__=='__main__':
    app.run(debug=True)
