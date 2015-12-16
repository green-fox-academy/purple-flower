from menu import Menu
from menu_item import MenuItem
from character import Character

user = ""

def new_game():
    user_name = input("Please enter your name: ")
    user = user_name
    print("Your character name is " + user_name + ".")
    new_game_submenu.display_menu()

def load_game():
    print("majd kesobb kitalalom")

def exit_game():
    exit()

def continue_game():
    continue_submenu.display_menu()

def save():
    save_submenu.display_menu()


def show_quit_submenu():
    quit_submenu.display_menu()

def quit_submenu():
    pass

def save_and_quit_submenu():
    pass

def resume():
    pass

def add_new_item():
    pass

def roll_stats():
    pass

main_menu = Menu([
    MenuItem(1, "New Game", new_game),
    MenuItem(2, "Load Game", load_game),
    MenuItem(3, "Exit", exit_game)
])

new_game_submenu = Menu([
    MenuItem(1, "Reenter name", new_game),
    MenuItem(2, "Continue", continue_game),
    MenuItem(3, "Save", save),
    MenuItem(4, "Quit", show_quit_submenu),
])

quit_submenu = Menu([
    MenuItem(1, "Save and Quit", save_and_quit_submenu),
    MenuItem(2, "Quit without save", quit_submenu),
    MenuItem(3, "Resume", resume)
])

save_submenu = Menu([
    MenuItem(1, "Add new item", add_new_item),
    MenuItem(2, "Resume", resume),
    MenuItem(3, "Quit", quit_submenu)
])

continue_submenu = Menu([
    MenuItem(1, "Reroll stats", roll_stats),
    MenuItem(2, "Continue", continue_game),
    MenuItem(3, "Save", save),
    MenuItem(4, "Quit", quit_submenu)
])

main_menu.display_menu()
