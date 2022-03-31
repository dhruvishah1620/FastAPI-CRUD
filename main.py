from fastapi import FastAPI, status, HTTPException
from database import Base, engine, TODO
from pydantic import BaseModel
from sqlalchemy.orm import Session

class ToDoRequest(BaseModel):
	task:str

Base.metadata.create_all(engine)

app = FastAPI()

@app.get('/')
def root():
	return "TODO"

@app.post("/todo",status_code=status.HTTP_201_CREATED)
def create_todo(todo: ToDoRequest):

	session = Session(bind=engine, expire_on_commit=False)

	Tododb = TODO(task = todo.task)

	session.add(Tododb)
	session.commit()

	task_id = Tododb.id

	session.close()

	return f"task created with id{task_id}"

@app.get("/todo/{id}")
def get_todo(id:int):

	session = Session(bind=engine,expire_on_commit=False)

	todo = session.query(TODO).get(id)

	session.close()

	if not todo:
		raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

	return todo

@app.put("/todo/{id}")
def update_todo(id:int):
	return "Update task by id"

@app.delete("/todo/{id}")
def delete_todo(id:int):
	return "Delete Task by id"

@app.get("/todo")
def getAll_todo():
	session = Session(bind=engine,expire_on_commit=False)

	tasks = session.query(TODO).all()

	session.close()

	return tasks