from flask import Flask, flash, render_template, url_for, redirect, request, session as flask_session
from database import *


app = Flask(__name__)
connected_user = ''
source = ''

@app.route('/')
def home():	
    return render_template("home.html")

@app.route('/user_signup' , methods = ['GET', 'POST'])
def user_signup():
    if request.method == 'GET':
        return render_template("user_signup.html")
    elif request.method == "POST":
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        username = request.form['username']
        password = request.form['password']

@app.route('/farm_signup', methods = ['GET', 'POST'])
def farm_signup():
    if request.method == 'GET':
        return render_template('farm_signup.html')
    elif request.method == "POST":
        farm_name = request.form['farmname']  
        farm_username = request.form['username']
        password = request.form['password']

@app.route('/user_login', methods = ['GET', 'POST'])
def user_login():
    if request.method == 'GET':
        return render_template('user_login.html')	


@app.route('/farm_login', methods = ['GET', 'POST'])
def farm_login():
    if request.method == 'GET':
        return render_template('farm_login.html')	

if __name__ == '__main__':
    app.run(debug=True)