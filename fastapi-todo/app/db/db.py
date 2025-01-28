from motor import motor_asyncio 

# connect database
client = motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
db = client.get_database('my_todo')
user_collection = db.get_collection('users')
todos_collection = db.get_collection('todos')