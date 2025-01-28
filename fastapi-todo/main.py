from fastapi import FastAPI
from app.router.auth import auth_router
from app.router.todo import todos_router

# Initialize app
app = FastAPI()

# Routers
app.include_router(auth_router, prefix='/auth')
app.include_router(todos_router, prefix='/todos')