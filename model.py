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
    Type = Column(String)
    Owner = Column(String)
    cost = Column(Float)

    def __repr__(self):
        return ("id : {},\n"
            "Type: {},\n"
            "Owner: {},\n"
            "cost: {}.\n"
            ).format(self.id_table,
                self.Type,
                self.Owner,
                self.cost)

class Type(Base):
    __tablename__ = "Types"
    id_table = Column(Integer, primary_key=True)
    Name = Column(String)
    Img = Column(String)
    Min_price = Column(Integer)
    Max_price = Column(Integer)
    def __repr__(self):
        return ("id : {},\n"
            "Name: {},\n"
            "img link: {},\n"
            "min_price: {}.\n"
            "max_price: {}.\n"
            ).format(self.id_table,
                self.Name,
                self.Img,
                self.Min_price,
                self.Max_price)