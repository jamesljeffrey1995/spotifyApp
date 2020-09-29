from application import app
from flask import render_template, redirect, url_for, request, Flask, jsonify, redirect
from flask_login import login_user, current_user, logout_user, login_required, current_user




@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    print("Hello")
    return render_template("home.html")
