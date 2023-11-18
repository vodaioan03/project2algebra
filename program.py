'''
Input: non-zero natural number n
Output:
  1. The number of bases of the vector space Zn2 over Z2
  2. The vector of each such basis(n<=4)
'''
import colorama
from colorama import Fore, Style
import random
import numpy as np
import math

def valid(option_chosen:str):
    if option_chosen.isnumeric() and int(option_chosen) in [1,2,3,4,5,6,7]:
        return True
    return False
  
def add_number_in_base_2(number:int):
  number_list = []
  while number > 0:
    number_list.append(number%10)
    number //= 10
  carry = 0
  if number_list[0] + 1 == 2:
    carry = 1
    number_list[0] = 0
  else:
    number_list[0] += 1
  counter = 1
  while carry != 0 and counter < len(number_list):
    if number_list[counter] + carry == 2:
      number_list[counter] = 0
      carry = 1
    else:
      number_list[counter] += carry
      carry = 0
    counter += 1
  if carry == 1:
    number_list.append(carry)
  multiplyer = 1
  for i in range(len(number_list)):
    number = number + number_list[i] * multiplyer
    multiplyer *= 10
  return number
      

def generate_posible_vector(length:int):
  number_initial = 10 ** length * 2
  last_num = 10 ** length
  list_of_vectors = []
  while last_num < number_initial :
    last_num = add_number_in_base_2(last_num)
    list_of_vectors.append(str(last_num)[1::])
  list_of_vectors.pop()
  return list_of_vectors

def choose_option():
    option = input("Choose option: ")
    if not valid(option):
        raise ValueError("You need to write a valid option!")
    try:
        option_proceed(int(option))
    except ValueError as e:
        print(Fore.RED + "ERROR: " + str(e) + Style.RESET_ALL)

def generate_list(length:int):
  posible_vector = generate_posible_vector(length)
  basis_list = []
  new_length = length
  posible_vector_l = len(posible_vector)
  number_of = 1
  while new_length > 0:
    number_of *= posible_vector_l
    posible_vector_l -= 1
    new_length -= 1
  generate_basis(posible_vector, 0,basis_list,length,0)
  print(f"The number of bases of the vector space Z2{length}  over Z2 is {number_of}")
      
def is_in_list(posible_list:list, elem:str):
  for i in posible_list:
    if i == elem:
      return False
  return True

def print_list(list_print:list,counter:int):
  string = '('
  for i in list_print:
    string += '('
    for j in i:
      string = string + j +','
    string = string[:-1] + '),'
  string = string[:-1]+')'
  print(f"{counter}. {string}")
  

def generate_basis(posible_vector:list, i:int,basis_list:list,length:int,counter:int):
  if len(basis_list) == length:
    counter += 1
    print_list(basis_list,counter)
    return counter
  elif len(basis_list) < length:
    for j in range(len(posible_vector)):
      if not is_in_list(basis_list,posible_vector[j]):
        continue
      basis_list.append(posible_vector[j])
      counter = generate_basis(posible_vector, j,basis_list,length,counter)
      basis_list.pop()
  return counter

def input_list():
  natural_number = input("Type a natural number: ").strip()
  if not natural_number.isnumeric():
    raise ValueError("You doesen't write a natural number!")
  natural_number = int(natural_number)
  if natural_number <= 0:
    raise ValueError("You doesen't write a natural number!")
  generate_list(natural_number)

def tests():
  generate_list(int(0))
  generate_list(int(1))
  generate_list(int(2))
  generate_list(int(3))
  generate_list(int(4))

def option_proceed(option_choosen:int):
  if option_choosen == 3:
    quit()
  if option_choosen == 2:
    tests()
  elif option_choosen == 1:
    try:
      input_list()
    except ValueError as e:
      print(Fore.RED + "ERROR: " + str(e) + Style.RESET_ALL)
  
def print_menu():
  print("Project 2 - Algebra [Voda Ioan]")
  print("1. Input natural number n.")
  print("2. Tests (0,1,2,3,4)")
  print("3. Exit")
  
def start():
  while True:
    print_menu()
    try:
      choose_option()
    except ValueError as e:
      print(Fore.RED + "ERROR: " + str(e) + Style.RESET_ALL)

if __name__ == "__main__":
  start()
  pass

