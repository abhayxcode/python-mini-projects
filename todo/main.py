import os
import time

# global list to store todos
todos = [] # maybe make a type strict array

# clear terminal
# clear terminal
# clear terminal
def clear_terminal():
  if os.name == 'nt':
    os.system('cls') 
  else:
    os.system('clear')


# Get all Todos
# Get all Todos
# Get all Todos
def getAllTodos():
  clear_terminal() # clear the interval
  
  if len(todos):
    print("All Todos:\n")
    for index, x in enumerate(todos):
      print(f"{index+1}. {x['task']} : {'done' if x['complete'] else 'pending'}")
    
    print("\n")
    todoIndex = int(input("Which todo to update? (press '0' for menu) : "))
  
    if todoIndex == 0:
      return
    elif todoIndex > len(todos):
      print('\nInvalid input!!')
      time.sleep(1)
    else:
      getTodoById(todoIndex)
  
  else:
    print('No Todos Available')
    time.sleep(1)

# Get Todo by Id
# Get Todo by Id
# Get Todo by Id
def getTodoById(todoIndex):
  clear_terminal()
  todo = todos[todoIndex - 1]
  print(f"Task: {todo['task']} - {'Finished' if todo['complete'] else 'pending'}")
  userInput = int(input(f"\n  1. Mark as {'pending' if todo['complete'] else 'Done'} \n  2. Delete Task \n\n Your choice (press '0' For Menu) : "))
  
  updateTodo(todoIndex,userInput)


# Add Todo
# Add Todo
# Add Todo
def addTodo():
  clear_terminal()
  task = input("\n  Add Task: ")
  todos.append({"id":len(todos) + 1,"task":task,"complete":False})
  time.sleep(0.1)
  print("\n  Todo added successfully\n")
  time.sleep(0.6)
  clear_terminal()

# Update/Delete Todo
# Update/Delete Todo
# Update/Delete Todo
def updateTodo(todoIndex, userInput):
  todo = todos[todoIndex - 1]
  if userInput == 1:
    todo['complete'] = False if todo['complete'] else True
  elif userInput == 2:
    del todos[todoIndex - 1]
  else:
    print("\n Invalid Input!")
    time.sleep(0.6)
    return

# Main function
# Main function
# Main function
def main():
  clear_terminal() # clear the interval
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