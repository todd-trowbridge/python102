todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

# this is my very first python function!

def print_todos():
  print('-----TODOS-----')
  # count starts at 1, index starts at 0
  count = 1
  for todo in todos:
    print(f"{count}: {todo}")
    count += 1
  print('-----TODOS-----')

while True:
  print ("""
Choose an option:

1. Print Todos
2. Add Todo
3. Remove Todo
0. Quit
  """)
  user_choice = input('')

  # print current todos
  if user_choice == '1':
    print_todos()
  
  # add new todo
  elif user_choice == '2':
    new_item = input('What do you want to add? ')
    todos.append(new_item)

  # delete a todo
  elif user_choice == '3':
    print_todos()
    delete_index = int(input('Which would you like to delete? '))
    del todos[delete_index - 1]

  # exit the program loop
  elif user_choice == '0':
    break