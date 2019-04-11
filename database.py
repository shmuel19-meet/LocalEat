from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind = engine)
session = DBSession()

"""
The function adds the user to the database given the parameters.
Input:  String username - The user's name.
		String email - The user's email.
		String phone - The user's phone.
		String city - The user's city.
		String address - The user's exact address.
Output: Boolean, if the operation was successful or not.
"""

def add_user(user_name, email, password, city, address):
    
	if phone.isdigit():
		session.add(User(name = user_name, password = password, email = email, city = city[0].upper() + city[1:].lower(), address = address.lower()))
		session.commit()
		return True
	return False

"""
The function returns the user which has the given user name.
Inpput: String name - The name of the user.
Output: The user with that name.
"""
def get_user_by_name(name):
	return session.query(User).filter_by(name = name).first()

"""
The function returns the user which has the given email.
Inpput: String email - The user's email.
Output: The user with that email.
"""
def get_user_by_email(email):
	return session.query(User).filter_by(email = email).first()

"""
The function checks if the password of the user with the given email or username matches the given password.
Inpput: String name - The name of the user or the user's email, String password - The password to check.
Output: Boolean, if the username matches the password.
"""
def is_the_user(name, password):

	return get_user_by_name(name).password == password or get_user_by_email(name).password == password
	
#================================================================================================================

"""
The function adds the farm to the database given the parameters.
Input:  String farm_name - The farm's name.
		String email - The farm's email.
		String phone - The farm's phone.
		String city - The farm's city.
		String address - The farm's exact address.
Output: Boolean, if the operation was successful or not.
"""

def add_farm(farm_name, email, phone, password, city, longitude, latitude):
    
	if phone.isdigit():
		session.add(Farm(name = farm_name[0].upper()+farm_name[1:].lower(), password = password, phone = phone, city = city[0].upper() + city[1:].lower(), longitude = longitude, latitude = latitude))
		session.commit()
		return True
	return False

"""
The function returns the farm with the given farm-name.
Input: String name - the farm's name.
Output: The farm with this farm-name.
"""
def get_farm_by_name(name):
	return session.query(Farm).filter_by(name = name).first()

"""
The function returns the farm with the given phone number.
Input: String phone - the farm's phone number.
Output: The farm with this phone number.
"""
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


def add_product(name, quantity, farm_id):
	ans = session.query(Product).filter_by(name = name, farm_id = farm_id).all() 
	if ans == None:
		session.add(Product(name = name, quantity = quantity, farm_id = farm_id))
	else
		ans.quantity += quantity
	session.commit()

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