from fastapi import FastAPI 
from app.models.user import User
from app.db.db import user_collection

# Initialize app
app = FastAPI()

#signup
@app.post('/signup')
async def signup(user:User): 
  # validate request
  
  # check for duplicate user
  
  # hash password
  
  # create user
  await user_collection.insert_one(user.model_dump(exclude='id'))

  # Return success message to user 
  return {'message':f'user created successfully'}

#signin

# Add todo

# Update todo

# delete todo

# Get all todos

# Get todo by Id
