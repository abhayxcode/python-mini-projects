from fastapi import FastAPI 
from app.models.user import User, Signin_Schema
from app.api.auth import signup, signin
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

# Add todo

# Update todo

# delete todo

# Get all todos

# Get todo by Id