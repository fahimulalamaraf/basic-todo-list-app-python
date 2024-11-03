import functions

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()



    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.set_todos (todos)


    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.title()
            row = f"{index + 1}.{item.strip('\n')}"
            print(row)


    elif user_action.startswith("edit"):

        try:

            number = int(user_action[5:])

            edited_user_action = input("Enter the new to-do: ") + '\n'

            number = number-1

            todos[number] = edited_user_action


            todos = functions.get_todos()

            print("Updated Successfully!")

        except ValueError:
            print("Please enter a number!")
            continue


    elif user_action.startswith("complete"):

        try:

            number = int(user_action[9:])
            index = number - 1

            removed_message =  todos[index].strip('\n')

            todos.pop(index)

            # Rewrite the updated to-do list in the text file
            functions.set_todos(todos)

            message = f"Todo {removed_message} was removed from the list"
            print(message)

        except ValueError:
            print("Please enter a number!")
            continue
        except IndexError:
            print("Please enter a number within the list!")
            continue

    elif user_action.startswith("exit"):
         break

    else:
        print("Command is not valid!")

print("Thank You for Using!")

