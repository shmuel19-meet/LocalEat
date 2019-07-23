from flask import Flask, flash, render_template, url_for, redirect, request ,jsonify, session  as flask_session
# from flask import Flask, flash, render_template, url_for, redirect, request, session as flask_session

from database import *
import paypalrestsdk

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'



paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AVNImnkNjDO_5NOS_qnWtEnAhDiVW-Wxcy88qJJ8SXBMQSD4G-wWx_ES8vDZLLgA6t4miS1J44My-GVg",
  "client_secret": "ENWdyCjvEEHUS9ycDdKaUpmnS4DmM7wT_qVc3aYQAZuFEv6OnnvAPfrZVZ2k5sgNEjgvbSzWfIJkoJ4R" })


@app.route('/')
def home():
    if 'username' in flask_session:
        username = flask_session['username']
        users_cash = get_users_cash(username)
        return render_template('User_HomePage.html',user=username,cash=users_cash)
    elif 'farmname' in flask_session:
        farmname = flask_session['farmname']
        return render_template('Farm_HomePage.html',farm=farmname,my_products=get_owner_products(farmname), log = False)
    else:
        return render_template('HomePage.html')

@app.route('/contact')
def Contact():
    Farm_list = get_all_farms()
    if 'username' in flask_session:
        Current_user =  flask_session['username']
        return render_template('Contact.html', Farm_list = Farm_list)
    else:
        return render_template('Contact.html', Farm_list = Farm_list)

@app.route('/shop')
def shop():
    if 'username' or 'farmname' in flask_session:
        update_min_max_types()
        return render_template('Shop.html',products=get_all_products(), types = get_all_Types())
    else:
        return redirect(url_for('user_logIn'))

@app.route('/add-product', methods =["GET","POST"])
def add_product():
    if 'farmname' in flask_session:
        if request.method =="GET":
            types = get_all_Types()
            return render_template('Add_Product.html', types = types)
        else:
            add_Product(request.form['category'],flask_session['farmname'],
                int(request.form['productcost']),"")
            return redirect(url_for('shop'))
    else:
        return redirect(url_for('shop'))

@app.route('/product/<string:Type>')
def product_page(Type):
    foodlist = get_type_products(Type)
    Type_1 = query_type_by_name(Type)
    return render_template('foodType.html', foodlist = foodlist, Type_1=Type_1)
    
@app.route('/user_sign-up', methods=['GET', 'POST'])
def user_signUp():
    if request.method == "POST":
        if query_user_by_username(request.form['username']) == None:
            if (request.form['password'] != request.form['Reenter_password']):
                flash('passwords dont match')
                return render_template('User_signup.html')
            else :
                add_User(request.form['username'],request.form['password'],request.form['phone'],request.form['address'],0)
                return redirect(url_for('user_logIn'))            
        else:
            flash('username already taken, please choose another one.')
            return render_template('User_signup.html')
    else:
        return render_template('User_signup.html')

@app.route('/farm_sign-up', methods=['GET', 'POST'])  
def farm_signUp():
    if request.method == "POST":
        if query_by_farmname(request.form['farmname']) == None:
            if (request.form['password']!=request.form['Reenter_password']):
                 flash('The password dont match')
                 return render_template('Farm_signup.html')
            else :
                add_Farm(request.form['farmname'],request.form['bank_name'],request.form['bank_account'],request.form['phone'],request.form['address'],request.form['password'])
                return redirect(url_for('farm_logIn'))
        else:
            flash('Farm name already taken, please choose another one.')
            return render_template('Farm_signup.html')
    else:
        return render_template('Farm_signup.html')

@app.route('/cart/<int:id_table>',methods=['GET','POST'])
def cart():
    if 'username' in flask_session:
        cartList = []
        return render_template('Cart.html',cartList=cartList)
    else:
        return redirect(url_for('shop'))

@app.route('/buy_product/<int:id_table>')
def buy_prduct(id_table):
    if 'username' in flask_session:
        product = query_product_by_id(id_table)
        username = flask_session['username']
        users_cash = get_users_cash(username)
        cartList = query_products_of_user(username)
        return render_template('User_HomePage.html',user=username,cash=users_cash,cartList=cartList)


@app.route('/user_log-in', methods=['GET','POST'])
def user_logIn():
    if request.method == "POST":
        user = query_by_username_and_password(request.form['username'], request.form['password'])

        if user is not None and user.password == request.form['password']:
            flask_session['username'] = user.username
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
            error = 'Farm name & Password do not match , Please try again'
            flash(error)
            return render_template('Farm_login.html')
    else:       
        return render_template('Farm_login.html')

@app.route('/user_log-out')
def user_logOut():
    if 'username' in flask_session:
        del flask_session['username']
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


# ########################################3
#@app.route('/payment/<str:', methods=['POST'],)
@app.route('/payment:', methods=['POST'],)
def payment():
    typeNeeded = get_type_products("")
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
        "payment_method": "paypal"},
        "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},
        "transactions": [{
        "item_list": {
            "items": [{
                "name": typeNeeded.name,
                # "sku": "1",
                "price": typeNeeded.cost ,
                "currency": "ISL",
                "quantity": 1}]},
        "amount": {
            "total": "",
            "currency": "ISL"},
        "description": "This is the payment transaction description."}]})
    if payment.create():
        print('payment success')
    else:
        print(payment.error)

	return jsonify({'paymentID' : 'PAYMENTID'})
#######################################

@app.route('/execute', methods=['POST'])
def execute():
	payment = paypalrestsdk.payment.find(request.form['paymentID'])
	
	if payment.execute({'payer_id'  : request.form['payerID']}):
		print('Execute success')
		success = True
	else:
		print(payment.error)

	return""

@app.route('/add_food_type', methods=['GET','POST'])
def add_Type():
    if request.method == "GET":
            return render_template('add_type.html')
    else:
        add_type(request.form['name'],request.form['img'],0,0)       
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

