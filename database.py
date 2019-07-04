from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///Data.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine))

def add_User(username, password,cash):
    try:
        user_object = User(username=username,
        password=password,cash=round(cash,2))
        session.add(user_object)
        session.commit()
    except:
        session.rollback()
        raise

def add_Farm(Farm_name,password):
    try:
        Farm_object = Farm(Farm_name=Farm_name,password=password)
        session.add(Farm_object)
        session.commit()
    except:
        session.rollback()
        raise    

def add_Product(name,Owner,cost):
  try:
    product_object = Product(name=name,Owner=Owner,cost=round(cost,2))
    session.add(product_object)
    session.commit()
  except:
    session.rollback()
    raise

def query_product_by_id(id):
   return  session.query(
       Product).filter_by(
       id_table=id).first() 


def update_cost_product_by_id(id):
    product = session.query(
       Product).filter_by(
       id_table=id).first()
    product.cost = 0
    session.commit()

def update_cash_user_by_username(username,cost):
    user = session.query(
       User).filter_by(
       username=username).first()
    user.cash -= cost
    session.commit()

def query_user_by_username(username):
   return  session.query(
       User).filter_by(
       username=username).first()

def query_by_farmname(farmname):
    return session.query(Farm).filter_by(Farm_name = farmname).first()

def delete_product_by_id(id):
    product = session.query(Product).filter_by(id_table=id).delete()
    session.commit()

def buy_product(username,product_id):
    user_cash = query_user_by_username(username).cash
    product_cost = query_product_by_id(product_id).cost

    if user_cash == product_cost or user_cash > product_cost:
        update_cash_user_by_username(username,product_cost)
        delete_product_by_id(product_id)
        return "bought"
    else:
        return "not enough cash"


def get_all_products():
    return session.query(Product).all()

def get_owner_products(Owner):
    return session.query(Product).filter_by(Owner=Owner).all()

def get_all_users():
    return session.query(User).all()


def query_by_username_and_password(username, password):
    return session.query(User).filter_by(username = username, password = password).first()

def query_by_farmname_and_password(farmname, password):
    return session.query(Farm).filter_by(Farm_name = farmname, password = password).first()

def delete_all_users():
    session.query(User).delete()
    session.commit()

def delete_all_products():
    session.query(Product).delete()
    session.commit()

