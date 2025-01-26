import json
import time
from utils.utils import  generate_random_id, clear_terminal, take_user_input
from todos.storage import load_from_json , save_to_json

# Global Todos variable
todos = load_from_json()

# Show menu
def show_menu():
  while(True):
    clear_terminal()
    user_choice = take_user_input("""Select Options:
      1. Show all Todos
      2. Add Todos
      3. Exit 
    
      Your choice: """)

    if (user_choice == 1):
      get_all_todos()
    elif (user_choice == 2):
      add_todo()
    elif (user_choice == 3):
      print('\n   Thankyou for using Todo_101 !!')
      time.sleep(1.2)
      clear_terminal()
      break
    elif user_choice == 'invalid':
      pass
    else:
      print('\n    Invalid Input!!!')
      time.sleep(0.8)

# Get All Todos
def get_all_todos():
  while(True):
    clear_terminal()

    if not todos:
      print('No Todos Available')
      time.sleep(1)
      break
  
    print("All Todos\n")
    for index,todo in enumerate(todos, start=1):  
      print(f" {index}. {todo['task']} : {  'Done' if todo['completed'] else 'Pending'}")
  
    user_input = take_user_input("\n    Select Todo (0 for back): ")

    if user_input == 'invalid':
      pass
    elif user_input > len(todos):
      print('\n    Invalid Input !!')
      time.sleep(0.8)
    elif user_input == 0:
      break
    else:
      get_todo_by_id(user_input)
     
# Add Todo
def add_todo():
  user_input = ''

  while(True):
    clear_terminal()
    # Take user input for Todo
    user_input = input("Add Todo: ").strip()

    # Check if user input is empty
    if not user_input:
      print("Task cannot be empty. Try again.")
      time.sleep(1)
    else: 
      break

  todos.append({"id": generate_random_id(), "task":user_input, "completed": False})

  save_to_json(todos)
  print('Todo Added Successfully!!')
  time.sleep(0.8)

# Get Todo by Id
def get_todo_by_id(index):
  while(True):
    todo = todos[index-1]

    clear_terminal()
    print(f"Current Todo: {todo['task']}\nStatus: {'Done' if todo['completed'] else 'Pending'}")

    user_input = take_user_input(f"\n1. Mark as {'Pending' if todo['completed'] else 'Done' } \n2. Delete Todo \n\nYour Choice (0 for back): ")

    if user_input == 'invalid':
      pass
    elif user_input == 0:
      break
    elif user_input == 1:
      update_todo(index)
    elif user_input == 2:
      delete_todo(index)
      break
    else:
      print('\n    Invalid Input!!')
      time.sleep(0.8)

# Update Todo  
def update_todo(index):
  print(f"\nMarked As {'Pending' if todos[index - 1]['completed'] else 'Done'} !!!")

  todos[index - 1]['completed'] = False if todos[index - 1]['completed'] else True
  save_to_json(todos)
  time.sleep(0.8)

# Delete Todo
def delete_todo(index):
  clear_terminal()
  del todos[index - 1]
  save_to_json(todos)
  print('Todo Deleted !!!')
  time.sleep(0.8)