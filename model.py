from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id_table = Column(Integer, primary_key = True)
    username = Column(String)
    phone = Column(Integer)
    address = Column(String)
    password = Column(String)
    cash = Column(Float)

    def __repr__(self):
        return ("username: {},\n"
            "phone: {},\n"
            "address: {},\n"
            "password: {}, \n"
            "cash: {}. \n"
            ).format(
                self.username,
                self.phone,
                self.address,
                self.password,
                self.cash)

class Farm(Base):
    __tablename__ = "Farm"
    id_table = Column(Integer, primary_key = True)
    Farm_name = Column(String)
    bank_name = Column(String)
    bank_account = Column(Integer)
    phone = Column(Integer)
    address = Column(String)
    password = Column(String)
    description = Column(String)

    def __repr__(self):
        return ("Farm_name: {},\n"
            "bank_name: {},\n"
            "bank_account: {},\n"
            "phone: {},\n"
            "address: {},\n"
            "password: {}, \n"
            "description: {}. \n"

            ).format(
                self.Farm_name,
                self.bank_name,
                self.bank_account,
                self.phone,
                self.address,
                self.password,
                self.description)

class Product(Base):
    __tablename__ = "products"
    id_table = Column(Integer, primary_key=True)
    Type = Column(String)
    Owner = Column(String)
    cost = Column(Float)
    buyer = Column(String)

    def __repr__(self):
        return ("id : {},\n"
            "Type: {},\n"
            "Owner: {},\n"
            "cost: {},\n"
            "buyer: {}.\n"
            ).format(self.id_table,
                self.Type,
                self.Owner,
                self.cost,
                self.buyer)

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

class Messages(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String)
    sender = Column(String)
    message = Column(String)
    time = Column(String)
    def __repr__(self):
        return str(self.id) + "+\n" + str(self.message)

class Online(Base):
    __tablename__ = "online"
    id = Column(Integer, primary_key = True)
    username = Column(String)