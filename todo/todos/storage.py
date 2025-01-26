import json

# Load all todos from json
def load_from_json():
   with open('data/todos.json' , 'r') as file:
    todos =  json.load(file)
    return todos

# Save todos to json
def save_to_json(todos):
  with open('data/todos.json' , 'w') as file:
    json.dump(todos,file,indent=4)
