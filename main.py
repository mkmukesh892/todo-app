# Todo terminal app
# from functions import get_todos, write_todos

import functions
while True:
    user_action = input('Enter you choice(add, show, edit, complete or exit):')
    user_action = user_action.strip()
    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:] +"\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:

            todos = functions.get_todos()

            index = int(user_action[5:]) - 1

            if index < 0 or index >= len(todos):
                print("Invalid todo number")
            else:
                edited_todo = input('Enter a todo:')
                todos[index] = f"{edited_todo}\n"

                functions.write_todos(todos)

                print(f'Todo number {index+1} edited successfully!')

        except ValueError:
            print('Invalid Todo Command')
            continue


    elif user_action.startswith('complete'):
        try:

            todos = functions.get_todos('todos.txt')

            index = int(user_action[9:]) - 1

            if index < 0 or index >= len(todos):
                print('Invalid todo number')
            else:
                deleted_todo = todos[index].strip('\n')
                todos.pop(index)

                functions.write_todos(todos)

                print(f'Todo "{deleted_todo}" completed successfully!')

        except ValueError:
            print('Todo Command is invalid')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid todo input")

print('Bye!')