import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label],[input_box, add_button]])

#read method opens the gui window with all the objects mentioned in the sg.Window()
window.read()
window.close()