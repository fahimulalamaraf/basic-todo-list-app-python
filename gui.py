import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")

# This key will get to-do in the key for tha map which will be inserted in the input box

input_box = sg.InputText(tooltip="Enter a To-Do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label],[input_box, add_button]],
                   font=("Helvetica", 16)
                   )


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values.get("todo") + "\n"
            todos.append(new_todo)
            functions.set_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
