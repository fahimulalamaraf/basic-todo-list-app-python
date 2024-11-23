import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")

# This key will get to-do in the key for tha map which will be inserted in the input box

input_box = sg.InputText(tooltip="Enter a To-Do", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=(44, 8))

edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                            font=("Helvetica", 16)
                   )


while True:     #Read method opens the gui window with all the objects mentioned in the sg.Window()
    event, values = window.read()
    print(1, event)    #Gets label of the button which was pressed
    print(2, values)   #Getting variables that were filled by the user
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values.get("todo") + "\n"
            todos.append(new_todo)
            functions.set_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case "Edit":
            todo_to_edit = values['todos'][0]       #values[todos] is giving us a list of a single string.
                                                    # [0] to access that element.
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.set_todos(todos)
            window['todos'].update(values=todos)

        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.set_todos(todos)
            window['todos'].update(values=todos)

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()