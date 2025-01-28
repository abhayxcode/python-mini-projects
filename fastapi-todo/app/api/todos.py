from app.models.todos import Todo
from app.db.db import todos_collection
from fastapi.responses import JSONResponse
from bson import ObjectId

# -------- Get all todos ---------
async def getall_todos():
  all_todos = await todos_collection.find().to_list(None)

  for todo in all_todos:
    todo['id'] = str(todo.pop('_id'))

  return JSONResponse(status_code=200,content={'message':'All Todos', "data": all_todos})

# -------- Get todo by id---------
async def get_todo_byid(id:str):
  try:
    todo_id = ObjectId(id)
  except:
    return JSONResponse(status_code=400, content={'message':'Invalid Object Id format'})

  # Find todo in database
  todo = await todos_collection.find_one({'_id':todo_id})

  if not todo:
    return JSONResponse(status_code=404,content={'message':'Todo with given id does not exist'})
 
  #  return todo to the client
  todo['id'] = str(todo.pop('_id'))
  return JSONResponse(status_code=200,content={'message':f"Todo with id {todo['id']}", "data": todo})


# -------- Add todo to db --------
async def add_todo(todo:Todo):
  todo.completed = False
  await todos_collection.insert_one(todo.model_dump(exclude='id'))

  return JSONResponse(status_code=200,content={'message':'Todo added successfully'})

# -------- Update todo --------
async def update_todo(todo:Todo):
  try:
    todo_id = ObjectId(todo.id)
  except:
    return JSONResponse(status_code=200,content={"message":"Invalid Todo Id"})

  # update todo
  await todos_collection.update_one({'_id':todo_id},{"$set": {'task':todo.task , 'completed':todo.completed}})

  return JSONResponse(status_code=200,content={'message':'Todo updated successfully'})

# -------- Delete todo --------
async def delete_todo(id:str):
  try:
    todo_id = ObjectId(id)
  except:
    return JSONResponse(status_code=400,content={'message':'Invalid todo id'})

  deleted_todo = await todos_collection.delete_one({'_id':todo_id})

  if not deleted_todo.raw_result['n']:
    return JSONResponse(status_code=404,content={'message':f'Todo with id {id} does not exist'})
    

  return JSONResponse(status_code=200,content={'message':'Todo deleted successfully'})
