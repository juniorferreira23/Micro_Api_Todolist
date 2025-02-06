from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from random import randint
from typing import Optional

class Task(BaseModel):
    name: str
    description: str
    is_done: bool = False
    completion_date: date

class TaskUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_done: Optional[bool] = None
    completion_date: Optional[date] = None
    
    
db = {}

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello world todo'}

@app.post('/task')
def register_task(task: Task):
    id = randint(1000,9999)
    db[id] = task
    return {'message': 'task register sucessfully'}
    
@app.get('/task')
def read_all_task():
    return db

@app.get('/task/{id_task}')
def read_by_id_task(id: int):
    if id not in db:
        return {'error': 'Task not foud'}
    return dict(filter(lambda x: x[0] == id, db.items()))

@app.patch('/task')
def update_task(id: int, task: TaskUpdate):
    if id not in db:
        return {'error': 'Task not foud'}
    updated_data = task.model_dump(exclude_unset=True)
    db[id] = db[id].model_copy(update=updated_data)     
    return {'message': 'task updated sucessfully'}

@app.delete('/task')
def delete_task(id: int):
    if id not in db:
        return {'error': 'Task not foud'}
    del db[id]
    return {'message': 'task deleted sucessfully'}
    


