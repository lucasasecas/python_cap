import tasks_module
import os

tasks = []
exit = False

def clean_screen():
  if os.name == 'posix':
    os.system('clear')
  elif os.name == 'nt':
    os.system('cls')

def print_menu(tasks):
  clean_screen()
  tasks_module.print_list(tasks)
  print("############")
  print("1. Insert item.")
  print("2. Delete item.")

def handle_option(option, ):
  global exit
  if option == 1:
    tasks_module.insert_task(tasks)
  elif option == 2:
    tasks_module.delete_task(tasks)
  else:
    exit = True

def main():
  tasks_module.print_list(tasks)
  while exit == False:
    print_menu(tasks)
    option = input("Select an option: ")
    option = int(option)
    handle_option(option)

if __name__ == "__main__":
  main()