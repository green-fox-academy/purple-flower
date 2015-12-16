from menu import Menu
from menu_item import MenuItem
from character import Character

user = Character()

def new_game():
    user_name = input("Please enter your name: ")
    user.name = user_name
    print("Your character name is " + user_name + ".")
    new_game_submenu.display_menu()

def load_game():
    print("majd kesobb kitalalom")

def exit_game():
    exit()

def continue_newgame():
    user.random_status()
    user.print_roll_status()
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


def continue_to_potion():
    print("Please choose a potion: ")
    choose_potion_submenu.display_menu()


def health_potion():
    user.inventory[0] = "Potion of Health"
    print("You have chosen: " + user.inventory[0])
    potion_submenu.display_menu()

def dexterity_potion():
    user.inventory[0] = "Potion of Dexterity"
    print("You have chosen: " + user.inventory[0])
    potion_submenu.display_menu()

def luck_potion():
    user.inventory[0] = "Potion of Luck"
    print("You have chosen: " + user.inventory[0])
    potion_submenu.display_menu()

def continue_begin():
    begin_submenu.display_menu()

def begin_game():
    pass


main_menu = Menu([
    MenuItem(1, "New Game", new_game),
    MenuItem(2, "Load Game", load_game),
    MenuItem(3, "Exit", exit_game)
])

new_game_submenu = Menu([
    MenuItem(1, "Reenter name", new_game),
    MenuItem(2, "Continue", continue_newgame),
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
    MenuItem(1, "Reroll stats", continue_newgame),
    MenuItem(2, "Continue", continue_to_potion),
    MenuItem(3, "Save", save),
    MenuItem(4, "Quit", quit_submenu)
])

choose_potion_submenu = Menu([
    MenuItem(1, "Potion of Health", health_potion),
    MenuItem(2, "Potion of Dexterity", dexterity_potion),
    MenuItem(3, "Potion of Luck", luck_potion)
])

potion_submenu = Menu([
    MenuItem(1, "Reselect the Potion", continue_to_potion),
    MenuItem(2, "Continue", continue_begin),
    MenuItem(3, "Quit", quit_submenu)
])

begin_submenu = Menu([
    MenuItem(1, "Begin", begin_game),
    MenuItem(2, "Save", save),
    MenuItem(3, "Quit", quit_submenu)
])

main_menu.display_menu()
