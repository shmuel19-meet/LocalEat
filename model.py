from sqlalchemy import Column, Integer, String, Boolean, Float 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	
	"""
	The user model is the template for the table to know what to contain.
	Fields:
	id - The number of the object in the column.
	name - The name of the user.
	password - The user's password.
	email - The email address of the user.
	city - The city the user lives in.
	"""
	
	__tablename__ = "Users"
	id = Column(Integer, primary_key = True)
	name = Column(String)
	password = Column(String)
	email = Column(String)
	city = Column(String)
	phone = Column(String)
	
class Farm(Base):
	
	"""
	The user model is the template for the table to know what to contain.
	Fields:
	id - The number of the object in the column.
	name - The name of the user.
	password - The user's password.
	email - The email address of the user.
	phone - The farm's phone number.
	longitude - The farm's longitude.
	latitude - The farm's latitude.
	"""
	
	__tablename__ = "Farms"
	id = Column(Integer, primary_key = True)
	name = Column(String)
	password = Column(String)
	email = Column(String)
	phone = Column(String)
	city = Column(String)
	longitude = Column(String)
	latitude = Column(String)

class Product(Base):
	
	__tablename__ = "Products"
	id = Column(Integer, primary_key = True)
	name = Column(String)
	quantity = Column(Integer)
	weight = Column(Float)
	price = Column(Float)
	fresh = Column(Boolean)
	fertilizer = Column(Boolean)
	modified = Column(Boolean)
	farm_id = Column(Integer)