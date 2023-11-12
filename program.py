'''
Input: non-zero natural number n
Output:
  1. The number of associative operations on a set A = {a1,a2,...,an}
  2. The operation table of each associative operation for (n<=4)
'''
import colorama
from colorama import Fore, Style
import random

def valid(option_chosen:str):
    if option_chosen.isnumeric() and int(option_chosen) in [1,2,3,4,5,6,7]:
        return True
    return False
  
def choose_option():
    option = input("Choose option: ")
    if not valid(option):
        raise ValueError("You need to write a valid option!")
    try:
        option_proceed(int(option))
    except ValueError as e:
        print(Fore.RED + "ERROR: " + str(e) + Style.RESET_ALL)
  
def test_one():
  pass  
def test_two():
  pass  
def test_three():
  pass  
def test_four():
  pass  
def test_five():
  pass  

def option_proceed(option_choosen:int):
  if option_choosen == 7:
    quit()
  elif option_choosen == 2:
    test_one()
  elif option_choosen == 3:
    test_two()
  elif option_choosen == 4:
    test_three()
  elif option_choosen == 5:
    test_four()
  elif option_choosen == 6:
    test_five()
  elif option_choosen == 1:
    pass
  
def print_menu():
  print("Project 2 - Algebra [Voda Ioan]")
  print("1. Input list of integers.")
  print("2. Test 1")
  print("3. Test 2")
  print("4. Test 3")
  print("5. Test 4")
  print("6. Test 5")
  print("7. Exit")
  
def start():
  while True:
    print_menu()
    try:
      choose_option()
    except ValueError as e:
      print(Fore.RED + "ERROR: " + str(e) + Style.RESET_ALL)

if __name__ == "__main__":
  start()