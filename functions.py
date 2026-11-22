def get_todos(filepath='todos.txt'):
    """Read todos from file and return a list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath='todos.txt'):
    """Write todos to file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_local)


if __name__ == '__main__':
    print(get_todos())