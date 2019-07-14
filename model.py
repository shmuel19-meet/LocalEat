from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id_table = Column(Integer, primary_key = True)
    email = Column(String)
    phone = Column(Integer)
    address = Column(String)
    
    password = Column(String)
    cash = Column(Float)

    def __repr__(self):
        return ("email: {},\n"
            "phone: {},\n"
            "address: {},\n"
            "password: {}, \n"
            "cash: {}.\n"
            ).format(
                self.email,
                self.phone,
                self.address,
                self.password,
                self.cash)

class Farm(Base):
    __tablename__ = "Farm"
    id_table = Column(Integer, primary_key = True)
    Farm_name = Column(String)
    password = Column(String)

    def __repr__(self):
        return ("Farm_name: {},\n"
            "password: {}. \n"
            ).format(
                self.Farm_name,
                self.password)

class Product(Base):
    __tablename__ = "products"
    id_table = Column(Integer, primary_key=True)
    name = Column(String)
    Owner = Column(String)
    cost = Column(Float)

    def __repr__(self):
        return ("id : {},\n"
            "name: {},\n"
            "Owner: {},\n"
            "cost: {}.\n"
            ).format(self.id_table,
                self.name,
                self.Owner,
                self.cost)