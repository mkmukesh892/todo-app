# Todo terminal app
while True:
    user_action = input('Enter you choice(add, show, edit, complete or exit):')
    user_action = user_action.strip().lower()
    match user_action:
        case "add":
            todo = input("Enter a todo:") +"\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item}"
                print(row)

        case "edit":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = int(input("Enter a todo Number:")) - 1

            if index < 0 or index >= len(todos):
                print("Invalid todo number")
            else:
                edited_todo = input('Enter a todo:')
                todos[index] = f"{edited_todo}\n"

                with open('todos.txt', 'w') as file:
                   file.writelines(todos)

                print(f'Todo number {index+1} edited successfully!')

        case "complete":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = int(input("Enter a Number:")) - 1

            if index < 0 or index >= len(todos):
                print('Invalid todo number')
            else:
                deleted_todo = todos[index].strip('\n')
                todos.pop(index)
                with open('todos.txt', 'w') as file:
                    file.writelines(todos)

                print(f'Todo "{deleted_todo}" completed successfully!')
        case "exit":
            break
        case _:
            print("Invalid todo input")

print('Bye!')