def insert_task(tasks):
  title = input("Task title: ")
  description = input("Task description: ")
  expiration_date = input("Expiration date (Format DD/MM/YYYY): ")
  task = (title, description, expiration_date)
  tasks.append(task)

def delete_task(tasks):
  position = input("Select a task to delete: ")
  try:
    op = int(position)
    del tasks[op]
  except ValueError:
    print("Invalid option. Press a key to continue.")
    input()

def print_list(tasks):
  if len(tasks) == 0:
    print("No tasks yet.")
  else:
    for i, task in enumerate(tasks):
      print(f"{i + 1}. {task[0]}")
      bar = '-' * len(f"{i + 1}. {task[0]}") 
      print(bar)
      print(task[1])
      print("")
      print(f"Expires at: {task[2]}")
