from flask import Flask, session
from flask import render_template
from flask import request, redirect

app = Flask(__name__)



@app.route('/')
def hello():
    return render_template("homepage.html")

@app.route('/login')
def login():
    return render_template