from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class User(Base):
	__tablename__ = "users"
	id = Column(Integer, primary_key = True)
	name = Column(String)
	password = Column(String)
	record = Column(Integer)
	
	def set_record(self, new_record):
	
		if new_record > self.record:
			self.record = new_record
	
	def get_record(self):
		return self.record