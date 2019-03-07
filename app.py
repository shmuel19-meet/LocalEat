from random import randint
from flask import Flask, request, redirect
from flask import render_template
import random
from database import *
import requests
import time

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
        age = request.form['age']




@app.route('/farm_signup', methods = ['GET', 'POST'])
def farm_signup():
    if request.method == 'GET':
        return render_template('farm_signup.html')
    elif request.method == "POST":
        farm_name = request.form['farmname']
        
        farm_username = request.form['username']
        password = request.form['password']
  


	# if request.method == 'GET':
	# 	return render_template('/templates/farmSignup.html', flag = False)
	
	# if request.method == 'POST' and get_user(request.form['username']) == None:
	# 	adduser(uname = request.form['userName'], upass = request.form['pass'], fname = request.form['farmName'], location = request.form['farmLocation'])
	# 	return redirect('/')
	
	# return redirect('login')

@app.route('/user_login', methods = ['GET', 'POST'])
def user_login():
    if request.method == 'GET':
        return render_template('user_login.html')	


@app.route('/farm_login', methods = ['GET', 'POST'])
def farm_login():
    if request.method == 'GET':
        return render_template('farm_login.html')	

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
	
# 	if request.method == 'GET':
# 		return render_template('/templates/login.html')
	
# 	if request.method == 'POST' and get_user(request.form['username'] == None):
# 		return redirect('/signup')
	
# 	return 'signup'

if __name__ == '__main__':
    app.run(debug=True)