from fastapi import APIRouter
from app.models.todos import Todo
from app.api.todos import getall_todos,get_todo_byid, add_todo, update_todo, delete_todo

todos_router = APIRouter()

# Get all todos
@todos_router.get('/')
async def getall_todos_handler():
  return await getall_todos()

# Get todo by Id
@todos_router.get('/{id}')
async def gettodo_byid_handler(id: str):
  return await get_todo_byid(id)

# Add todo
@todos_router.post('/')
async def add_todo_handler(todo:Todo):
  return await add_todo(todo)

# Update todo
@todos_router.put('/')
async def update_todo_handler(todo:Todo):
  return await update_todo(todo)

# delete todo
@todos_router.delete('/{id}')
async def delete_todo_handler(id:str):
  return await delete_todo(id)