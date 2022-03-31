from fastapi import FastAPI, status
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///TodoDB.db")

Base = declarative_base()

class TODO(Base):
	__tablename__ = 'TODO'
	id = Column(Integer,primary_key=True)
	task = Column(String(220))

Base.metadata.create_all(engine)

app = FastAPI()

@app.get('/')
def root():
	return "TODO"

@app.post("/todo",status_code=status.HTTP_201_CREATED)
def create_todo():
	return "create task"

@app.get("/todo/{id}")
def get_todo(id:int):
	return "Get task by id"

@app.put("/todo/{id}")
def update_todo(id:int):
	return "Update task by id"

@app.delete("/todo/{id}")
def delete_todo(id:int):
	return "Delete Task by id"

@app.get("/todo")
def getAll_todo():
	return "Get all task"