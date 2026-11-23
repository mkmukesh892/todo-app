FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """Read todos from file and return a list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """Write todos to file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_local)


if __name__ == '__main__':
    print(get_todos())