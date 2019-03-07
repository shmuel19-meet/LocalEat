from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(username, password):
    
	session.add(User(name = username, password = password, record = 0))
	session.commit()
	
def get_user(name):
	
	return session.query(User).filter_by(name = name).first()

def set_new_record(name, new_record):

	user = get_user(name)
	print(user)
	user.set_record(new_record)
	session.add(user)
	session.commit()

def is_the_user(name, password):
	return get_user(name).password == password