from fastapi import FastAPI, status, HTTPException
from database import Base, engine
from sqlalchemy.orm import Session
import models
import schemas

Base.metadata.create_all(engine)

app = FastAPI()

@app.get('/')
def root():
	return "TODO"

@app.post("/todo",status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoRequest):

	session = Session(bind=engine, expire_on_commit=False)

	Tododb = models.TODO(task = todo.task)

	session.add(Tododb)
	session.commit()

	task_id = Tododb.id

	session.close()

	return f"task created with id{task_id}"

@app.get("/todo/{id}")
def get_todo(id:int):

	session = Session(bind=engine,expire_on_commit=False)

	todo = session.query(models.TODO).get(id)

	session.close()

	if not todo:
		raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

	return todo

@app.put("/todo/{id}")
def update_todo(id:int, todoTask:schemas.ToDoRequest):

	session = Session(bind=engine,expire_on_commit=False)

	todo = session.query(models.TODO).get(id)

	if todo:
		todo.task = todoTask.task
		session.commit()
		session.close()
		return todo
	else:
		raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
	

@app.delete("/todo/{id}")
def delete_todo(id:int):

	session = Session(bind=engine,expire_on_commit=False)

	todo = session.query(models.TODO).get(id)

	if todo:
		session.delete(todo)
		session.commit()
		session.close()
		return "Task deleted successfully"
	else:
		raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

@app.get("/todo")
def getAll_todo():
	session = Session(bind=engine,expire_on_commit=False)

	tasks = session.query(models.TODO).all()

	session.close()

	return tasks