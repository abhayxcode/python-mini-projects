import json
from pathlib import Path

DATA_FILE= Path('data/todos.json')

# Load all todos from json
def load_from_json():
  if not DATA_FILE.exists():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text("[]") 

  with open('data/todos.json' , 'r') as file:
    todos =  json.load(file)
    return todos

# Save todos to json
def save_to_json(todos):
  with open('data/todos.json' , 'w') as file:
    json.dump(todos,file,indent=4)
