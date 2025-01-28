from fastapi import APIRouter
from app.models.user import User, Signin_Schema
from app.db.db import user_collection
from fastapi.responses import JSONResponse
import bcrypt 
import jwt

# --------- Signup Function ---------
async def signup(user:User):   
  # check for duplicate user
  existing_user = await user_collection.find_one({"email" : user.email})

  if existing_user:
    return JSONResponse(status_code=409, content={'message':"User with this email already exists"})

  # hash password
  bytes = user.password.encode('utf-8')
  salt = bcrypt.gensalt()
  hash_password = bcrypt.hashpw(bytes,salt)
  user.password = hash_password.decode('utf-8')

  # create user
  await user_collection.insert_one(user.model_dump(exclude='id'))

  # Return success message to user 
  return JSONResponse(
        content={'message': 'User created successfully'},
        status_code=201
    )


# --------- Signin Function ---------
async def signin(user: Signin_Schema):
  # check if user exists
  existing_user = await user_collection.find_one({'email':user.email})

  if not existing_user:
    return JSONResponse(status_code=404,content={'message':'Email and password do not match'})

  # compare password
  password_match = bcrypt.checkpw(user.password.encode('utf-8'), existing_user['password'].encode('utf-8'))

  if not password_match:
    return JSONResponse(status_code=404,content={'message':'Email and password do not match'})

  # Generate token
  encoded_jwt = jwt.encode({'id':str(existing_user['_id']), 'email':existing_user['email']} , 'JWT123456' , algorithm='HS256')

  # Return token
  return JSONResponse(status_code=200, content={'message':'Signin Successful' , 'token': encoded_jwt})
