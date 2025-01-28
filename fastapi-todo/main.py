from fastapi import FastAPI 
from app.models.user import User, Signin_Schema
from app.models.todos import Todo
from app.api.auth import signup, signin
from app.api.todos import getall_todos,get_todo_byid, add_todo, update_todo, delete_todo

# Initialize app
app = FastAPI()

#signup
@app.post('/signup')
async def signup_handler(user: User):
  return await signup(user)

#signin
@app.post('/signin')
async def signin_handler(user:Signin_Schema):
  return await signin(user)

# Get all todos
@app.get('/todos')
async def getall_todos_handler():
  return await getall_todos()

# Get todo by Id
@app.get('/todos/{id}')
async def gettodo_byid_handler(id: str):
  return await get_todo_byid(id)

# Add todo
@app.post('/todos')
async def add_todo_handler(todo:Todo):
  return await add_todo(todo)

# Update todo
@app.put('/todos')
async def update_todo_handler(todo:Todo):
  return await update_todo(todo)

# delete todo
@app.delete('/todos/{id}')
async def delete_todo_handler(id:str):
  return await delete_todo(id)

