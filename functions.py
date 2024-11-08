FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Get the todos from the text file into the todos list."""

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        for item in todos_local:
            item = item.title()
    return todos_local

def set_todos(updated_todos, filepath=FILEPATH):
    """Set the updated todos in my text file"""

    with open(filepath, 'w') as file_local:
        file_local.writelines(updated_todos)

#When this file is running __name__ will be main and
# when this file is being imported to another file,
# the __name__ will be the name of the file


if __name__ == "__main__":
    print(get_todos())