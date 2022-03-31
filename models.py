from sqlalchemy import Column, Integer, String
from database import Base

class TODO(Base):
	__tablename__ = 'TODO'
	id = Column(Integer,primary_key=True)
	task = Column(String(220))