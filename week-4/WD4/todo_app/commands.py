import json
from datetime import datetime, timezone
import submenu

def load():
    todo = []
    input_file = open("todo_items.json", "r")
    try:
        todo = json.load(input_file)
    except Exception as e:
        pass
    input_file.close()
    return todo

def save(todo):
    output_file = open("todo_items.json", "w")
    json.dump(todo, output_file)
    output_file.close()


def add_item(todo):
    desc = input("\033[34m" + "Description: " + "\033[39m")
    input_date = input("\033[34m" + "Enter the due date. (Please use the following format: 2015-12-03)" + "\033[39m")
    todo.append({"due date": input_date, "status": "to do", "description": desc})
    save(todo)

def list_item(todo):
    if todo != []:
        i = 1
        for n in todo:
            print(i, n["due date"] + " \\ " + n["description"] + " \\ " + n["status"])
            i += 1
    else:
        print("\033[34m" + "You don\'t have nothing to do!" + "\033[39m")


def change_status_item(todo):
    if todo != []:
        status_item_rang = int(input("\033[34m" + "Which to do item\'s status would you like to change?" + "\033[39m"))
        submenu.print_status_submenu()
        status_number = int(input("\033[34m" + "What will be your to do item\'s new status?" + "\033[39m"))
        n = status_item_rang - 1
        if status_number == 1:
            todo[n]["status"] = "to do"
        elif status_number == 2:
            todo[n]["status"] = "in progress"
        elif status_number == 3:
            todo[n]["status"] = "done"
        else:
            print("\033[34m" + "Please choose a number from the menu!" + "\033[39m")
        save(todo)
    else:
        print("\033[34m" + "Your list is empty." + "\033[39m")

def remove_completed_items(todo):
    if todo != []:
        for item in todo:
            if item["status"] == "done":
                todo.remove(item)
        print("\033[34m" + "All done items are deleted." + "\033[39m")
        save(todo)
    else:
        print("\033[34m" + "Your list is empty." + "\033[39m")

def remove_item(todo):
    if todo != []:
        removed_item_rang = int(input("Which to do item would you like to remove?"))
        n = removed_item_rang - 1
        todo.pop(n)
        save(todo)
    else:
        print("\033[34m" + "Your list is empty." + "\033[39m")
