from flask import Flask, flash, render_template, url_for, redirect, request, session as flask_session
from database import *

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/')
def home():
    if 'username' in flask_session:
        email = flask_session['email']
        return render_template('User_HomePage.html',user=email)
    elif 'farmname' in flask_session:
        farmname = flask_session['farmname']
        return render_template('Farm_HomePage.html',farm=farmname,my_products=get_owner_products(farmname))
    else:
        return render_template('HomePage.html')

@app.route('/shop')
def shop():
    if 'username' or 'farmname' in flask_session:
        return render_template('Shop.html',products=get_all_products())
    else:
        return redirect(url_for('user_logIn'))

@app.route('/add-product', methods =["GET","POST"])
def add_product():
    if 'farmname' in flask_session:
        if request.method =="GET":
            return render_template('Add_Product.html')
        else:
            add_Product(request.form['productname'],flask_session['farmname'],
                int(request.form['productcost']))
            return redirect(url_for('shop'))
    else:
        return redirect(url_for('shop'))

@app.route('/product/<int:id>')
def product_page(id):
    return render_template('Product.html', name = query_product_by_id(id).name,
        Owner=query_product_by_id(id).Owner,cost=query_product_by_id(id).cost)

    
@app.route('/user_sign-up', methods=['GET', 'POST'])
def user_signUp():
    if request.method == "POST":
        if query_user_by_username(request.form['email']) == None:
            add_User(request.form['email'],request.form['password'],request.form['phone'],request.form['address'],0)
            return redirect(url_for('user_logIn'))
        else:
            flash('User name already taken, please choose another one.')
            return render_template('User_signup.html')            
    else:
        return render_template('User_signup.html')

@app.route('/farm_sign-up', methods=['GET', 'POST'])  
def farm_signUp():
    if request.method == "POST":
        if query_by_farmname(request.form['farmname']) == None:
            add_Farm(request.form['farmname'],request.form['phone'],request.form['address'],request.form['password'])
            return redirect(url_for('farm_logIn'))
        else:
            flash('Farm name already taken, please choose another one.')
            return render_template('Farm_signup.html')
    else:
        return render_template('Farm_signup.html')

@app.route('/user_log-in', methods=['GET','POST'])
def user_logIn():
    if request.method == "POST":
        user = query_by_username_and_password(request.form['email'], request.form['password'])

        if user is not None and user.password == request.form['password']:
            flask_session['email'] = user.username
            return redirect(url_for('home'))
        else:
            error = 'Username & Password do not match , Please try again'
            flash(error)
            return render_template('User_login.html')
    else:       
        return render_template('User_login.html')

@app.route('/farm_log-in', methods=['GET','POST'])
def farm_logIn():
    if request.method == "POST":
        farm = query_by_farmname_and_password(request.form['farmname'], request.form['password'])

        if farm is not None and farm.password == request.form['password']:
            flask_session['farmname'] = farm.Farm_name
            return redirect(url_for('home'))
        else:
            return render_template('Farm_login.html')
    else:       
        return render_template('Farm_login.html')

@app.route('/user_log-out')
def user_logOut():
    if 'email' in flask_session:
        del flask_session['email']
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

@app.route('/farm_log-out')
def farm_logOut():
    if 'farmname' in flask_session:
        del flask_session['farmname']
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

