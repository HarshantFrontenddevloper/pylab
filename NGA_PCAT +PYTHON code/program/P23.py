# create a program that  manage a shopping lists. users can add items to the list remove items and list  of items
import os

def clear_console():
 os.system('cls' if os.name == 'nt' else 'clear')
#creating the empty list
shopping_list = []
# function to display the item of the shooping list
def display_list():
 if not shopping_list:
  print("The Shopping list is empty..")
 else:
  print("The shoping lists are follows: ")
  for item in shopping_list:
   print(f"- {item}")


# function  for adding the item in the shopping list

def add_item(item):
 shopping_list.append(item)
 print(f"{item} - is added in the shopping list.")


# function  to remove the element from  the lists

def remove_item(item):
 if item in shopping_list:
  shopping_list.remove(item)
  print(f"{item} has been removed from the shopping list.")
 else:
  print(f"{item} in not in the list")



# main program

while True:
 print("\n1. Add item to shopping list")
 print("\n2. remove item to shopping list")
 print("\n3. display item to shopping list")
 print("\n4. Exits ")

 choice = input("Enter your choice (1-4): ")

 if choice == "1":
  item_to_add = input("Enter the item  to add:")
  add_item(item_to_add)
 elif choice == "2":
  item_to_remove = input("Enter the item to remove: ")
  remove_item(item_to_remove)
 elif choice == "3":
  display_list()
 elif choice == "4":
  print("Exiting program ....")
  break
 else: 
  print("Invaild choice. Please enter a number from  1 to 4")

 
   