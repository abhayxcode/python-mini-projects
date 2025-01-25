import time
import platform
import os
import random
import math

# Clear Terminal
def clear_terminal():
  if(platform.system == 'Windows'):
    os.system('cls')
  else:
    os.system('clear') 

# Take yours choice
def take_user_input(text:str):
    user_input = input(text)
    
    if user_input.isdigit() and len(user_input) == 1:
      return int(user_input)
    else:
      print('\n   Invalid Input! Please make a valid choice')
      time.sleep(1)
      return 'invalid'
      
# Generate random id
def generate_random_id():
  id = str(math.floor((random.uniform(0,1) * 10000000000)))

  return id