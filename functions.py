def get_todos(filepath="todos.txt"):
    """Get the todos from the text file into the todos list."""

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def set_todos(updated_todos, filepath = "todos.txt"):
    """Set the updated todos in my text file"""

    with open(filepath, 'w') as file_local:
        file_local.writelines(updated_todos)