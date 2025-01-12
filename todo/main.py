import os
import time
import json
import uuid

# global list to store todos
todos = [] # maybe make a type strict array

# **************
# clear terminal
# **************
def clear_terminal():
  if os.name == 'nt':
    os.system('cls') 
  else:
    os.system('clear')

# *************
# Get all Todos
# *************
def getAllTodos() -> None:
  clear_terminal()
  
  if len(todos):
    print("All Todos:\n")
    for index, x in enumerate(todos):
      print(f"{index+1}. {x['task']} : {'done' if x['complete'] else 'pending'}")
    
    print("\n")
    try:
      todoIndex = int(input("Which todo to update? (press '0' for menu) : "))
    except:
      todoIndex = 'invalid'

    if todoIndex == 0:
      return
    elif todoIndex == 'invalid' or todoIndex > len(todos)  :
      print('\nInvalid input!!')
      time.sleep(1)
    else:
      getTodoById(todoIndex)
  
  else:
    print('No Todos Available')
    time.sleep(0.8)

# **************
# Get Todo by Id
# **************
def getTodoById(todoIndex:int) -> None:
  clear_terminal()
  todo = todos[todoIndex - 1]
  print(f"Task: {todo['task']} - {'Finished' if todo['complete'] else 'pending'}")

  try:
    userInput = int(input(f"\n  1. Mark as {'pending' if todo['complete'] else 'Done'} \n  2. Delete Task \n\n Your choice (press '0' For Menu) : "))
  except:
    userInput = 'invalid'
  
  if userInput == 1 or userInput == 2:
    updateTodo(todoIndex,userInput)
  else:
    print('\n  Invalid Input')
    return

# ********
# Add Todo
# ********
def addTodo() -> None:
  clear_terminal()

  task = input("\n  Add Task: ")
  
  todos.append({"id": str(uuid.uuid4()) ,"task":task,"complete":False})
  
  saveToJsonFile()
  
  time.sleep(0.1)
  print("\n  Todo added successfully\n")
  time.sleep(0.6)

# ******************
# Update/Delete Todo
# ******************
def updateTodo(todoIndex : int, userInput:int) -> None:
  todo = todos[todoIndex - 1]
  if userInput == 1:
    todo['complete'] = False if todo['complete'] else True
    saveToJsonFile()
  elif userInput == 2:
    del todos[todoIndex - 1]
    saveToJsonFile()
  else:
    print("\n Invalid Input!")
    time.sleep(0.6)
    return
  
# *****************
# Save to Json file
# *****************
def saveToJsonFile():
  with open('todos.json','w') as file:
    json.dump(todos , file , indent=4)

# *******************************
# Load saved todos from json file
# *******************************
def loadTodosFromJson():
  try:
    with open('todos.json','r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []

# *************
# Main function
# *************
def main():
  clear_terminal() # clear the interval

  global todos
  todos = loadTodosFromJson()
  while True:
    try:
      clear_terminal() # clear the interval
      try:
        userInput = int(input("""Select an option:
  1. Show all todos
  2. Add new Todo
  3. Exit
      
  Your Choice: """))
      except:
        userInput = 'invalid'

      if userInput == 1:
        getAllTodos()

      elif userInput == 2:
        addTodo()

      elif userInput == 3:
       print('\n  Thank you for visiting!!!')
       time.sleep(1)
       break
      
      else:
        time.sleep(0.2)
        print('\n  Invalid input!!!')
        time.sleep(0.6)
    

    except:
      print("\n\nSomething went wrong")
      break

main()