# uvicorn main:app --reload
# http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app= FastAPI()

class Todo(BaseModel):
    id:int 
    task: str
    completed: bool = False


class TodoCreate(BaseModel):
    task: str
    completed: bool = False

todos =[
    Todo(id=1, task="clean the bed", completed= False),
    Todo(id= 2, task= "Complete ALC assignment", completed= False),
    Todo(id=3, task=" make dinner", completed= False)
]

#create task
@app.post("/todos")
def create_todo(todo: TodoCreate):
    new_id = len(todos) + 1
    new_todo = Todo(id=new_id, task=todo.task, completed=todo.completed)
    todos.append(new_todo)
    return new_todo

#reading all todos
@app.get("/todos")
def view_todos():
    return todos

#reading specific task
@app.get("/todos/{todo_id}")
def get_one_todo(todo_id: int):
    for todo in todos: #1-3
        if todo.id== todo_id:
            return todo
    raise HTTPException(status_code=404, detail="todo not found")


# edit existing task
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            # ensure the id remains consistent
            updated = Todo(id=todo_id, task=updated_todo.task, completed=updated_todo.completed)
            todos[index] = updated
            return updated
    raise HTTPException(status_code= 404, detail= " todo id not found")

# delete a task
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted_todo= todos.pop(index)
            return {"message": "todo deleted successfully"}
    raise HTTPException(status_code=404, detail ="todo not found")
    
