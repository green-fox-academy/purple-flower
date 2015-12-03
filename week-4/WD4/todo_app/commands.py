import json

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
    desc = input("Description: ")
    todo.append({"status": "to do", "description": desc})
    save(todo)

def list_item(todo):
    i = 1
    for n in todo:
        print(i, n["status"], n["description"])
        i += 1

def complete_item(todo):
    completed_item_rang = int(input("Which to do item would you like to set done?"))
    n = completed_item_rang - 1
    todo[n]["status"] = "done"
    save(todo)


def remove_item(todo):
    removed_item_rang = int(input("Which to do item would you like to remove?"))
    n = removed_item_rang - 1
    todo.pop(n)
    save(todo)

"""def remove_all_completed(input_file):
    for"""
