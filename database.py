from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///TodoDB.db")

Base = declarative_base()

class TODO(Base):
	__tablename__ = 'TODO'
	id = Column(Integer,primary_key=True)
	task = Column(String(220))
