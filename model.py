from sqlalchemy import Column, Integer, String, Boolean, Float 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):	
	__tablename__ = "Users"
	id_table = Column(Integer, primary_key = True)
	username = Column(String)
	password = Column(String)
	email = Column(String)
	phone = Column(String)
	
class Farm(Base):
	
	__tablename__ = "Farms"
	id_table = Column(Integer, primary_key = True)
	Farm_name = Column(String)
	password = Column(String)
	email = Column(String)


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
	