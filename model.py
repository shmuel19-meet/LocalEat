from sqlalchemy import Column, Integer, String, Boolean
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
	address - The user's address.
	"""
	
	__tablename__ = "Users"
	id = Column(Integer, primary_key = True)
	name = Column(String)
	password = Column(String)
	email = Column(String)
	city = Column(String)
	address = Column(String)
	
class Farm(Base):
	
	"""
	The user model is the template for the table to know what to contain.
	Fields:
	id - The number of the object in the column.
	name - The name of the user.
	password - The user's password.
	email - The email address of the user.
	phone - The farm's phone number.
	location - The farm's location.
	"""
	
	__tablename__ = "Farms"
	id = Column(Integer, primary_key = True)
	name = Column(String)
	password = Column(String)
	email = Column(String)
	phone = Column(String)
	city = Column(String)
	address = Column(String)
	