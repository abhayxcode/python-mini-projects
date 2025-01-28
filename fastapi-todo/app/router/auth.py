from fastapi import  APIRouter
from app.models.user import User, Signin_Schema
from app.api.auth import signup, signin

# Routers
auth_router = APIRouter()

#signup
@auth_router.post('/signup')
async def signup_handler(user: User):
  return await signup(user)

#signin
@auth_router.post('/signin')
async def signin_handler(user:Signin_Schema):
  return await signin(user)
