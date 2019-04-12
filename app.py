from flask import Flask, flash, render_template, url_for, redirect, request, session as flask_session
from database import *
import time

app = Flask(__name__)
connected_user = ''
source = ''
app.secret_key = 'LocalEat'

@app.route('/')
def home():	
    return render_template("home.html")

@app.route('/user_signup' , methods = ['GET', 'POST'])
def user_signup():
    if request.method == 'GET':
        return render_template("user_signup.html")

    elif request.method == "POST":
        city = request.form['City']
        username = request.form['Username']
        password = request.form['Password']
        email = request.form['Email']
        phone = request.form['Phone']
        print(city, username, password, email, phone)
        add_user(city = city, name = username, password = password, email = email, phone = phone)
        return redirect(url_for('user_login'))

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
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']

        user = is_the_user(name, password)

        if user is not None and user.password == password:
            flask_session['username'] = user.name
            return redirect(url_for('home'))
        else :
            error = 'Username & Password do not match , Please try again'
            flash(error)
            return render_template('user_login.html')
    else:       
        return render_template('user_login.html')	


@app.route('/farm_login', methods = ['GET', 'POST'])
def farm_login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']

        user = is_the_farm(name, password)

        if user is not None and user.password == password:
            flask_session['username'] = user.name
            return redirect(url_for('home'))
        else :
            error = 'Username & Password do not match , Please try again'
            flash(error)
            return render_template('farm_login.html')
    else:       
        return render_template('farm_login.html')   
if __name__ == '__main__':
    app.run(debug=True)