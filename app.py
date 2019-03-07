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
	
	return redirect('/signup')

@app.route('/farmsignup', methods = ['GET', 'POST'])
def farm_sign_up():
	
	if request.method == 'GET':
		return render_template('/templates/farmSignup.html', flag = False)
	
	if request.method == 'POST' and get_user(request.form['username']) == None:
		adduser(uname = request.form['userName'], upass = request.form['pass'], fname = request.form['farmName'], location = request.form['farmLocation'])
		return redirect('/')
	
	return redirect('login')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	
	if request.method == 'GET':
		return render_template('/templates/login.html')
	
	if request.method == 'POST' and get_user(request.form['username'] == None):
		return redirect('/signup')
	
	return 'signup'

if __name__ == '__main__':
    app.run(debug=True)