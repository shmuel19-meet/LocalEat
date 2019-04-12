from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind = engine)
session = DBSession()


def add_user(username, password,email,phone):
    user_object = User(username=username,
     password=password,
     email=email,
     phone=phone)
    session.add(user_object)
    session.commit()


def get_user_by_name(name):
	return session.query(User).filter_by(name = name).first()

def get_user_by_email(email):
	return session.query(User).filter_by(email = email).first()

def query_by_name_and_password(username, password):
    return session.query(User).filter_by(username = username, password = password).first()

	
def add_farm(Farm_name, email,password):
    farm_object = Farm(Farm_name=Farm_name,
     password=password,
     email=email)
    session.add(user_object)
    session.commit()	

def query_by_Farm_name_and_password(Farm_name, password):
    return session.query(User).filter_by(Farm_name = Farm_name, password = password).first()


def get_farm_by_name(name):
	return session.query(Farm).filter_by(name = name).first()

def get_farm_by_phone(phone):
	return session.query(Farm).filter_by(phone = phone).first()

"""
The function returns the farm with the given email address.
Input: String email - the farm's email address.
Output: The farm with this email address.
"""
def get_farm_by_email(email):
	return session.query(User).filter_by(email = email).first()

"""
The function returns all farms in the given city.
Input: String city - the city to filter by.
Output: The list of farms in this city.
"""
def get_farms_by_city(city):
	return session.query(Farm).filter_by(city = city).all()

"""
The function checks if the password of the farm with the given email or username matches the given password.
Inpput: String name - The name of the farm or the farm's email, String password - The password to check.
Output: Boolean, if the farm-name matches the password.
"""	
def is_the_farm(name, password):
	return get_farm_by_name(name).password == password


def add_product(name, quantity, weight, price, fresh, fertilizer, modified):
	
	add = ADD(
		name = name,
		quantity = quantity,
		weight = weight,
		price = price,
		fresh = fresh,
		fertilizer = fertilizer,
		modified = modified)
	session.add(add)
	session.commit()

# ans = session.query(Product).filter_by(name = name, farm_id = farm_id).all() 
	# if ans == None:
	# 	session.add(Product(name = name, quantity = quantity, farm_id = farm_id))
	# else:
	# 	ans.quantity += quantity
	# session.commit()

def buy_product(name, farm_id):
	ans = session.query(Product).filter_by(name = name, farm_id = farm_id).first()
	if ans == None:
		return False

	ans.quantity -= quantity
	session.commit()
	return True

def get_product(name, farm_id):
	ans = session.query(Product).filter_by(name = name, farm_id = farm_id).first()
	return ans
<<<<<<< HEAD



=======
>>>>>>> fc0f9e4479c6b0e10cc66dadb6d24a253e1a4c35
