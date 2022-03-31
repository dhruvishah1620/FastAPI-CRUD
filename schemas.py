from pydantic import BaseModel

class ToDoRequest(BaseModel):
	task:str
