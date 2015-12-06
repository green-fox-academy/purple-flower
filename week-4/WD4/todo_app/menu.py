import commands
from datetime import datetime, timezone


def print_menu():
    print("                                                              ")
    print("                                                              ")
    print("**************************************************************")
    print("*                           MENU                             *")
    print("*                                                            *")
    print("*       1 list items                                         *")
    print("*       2 add item                                           *")
    print("*       3 change item status                                 *")
    print("*       4 remove item from the list                          *")
    print("*       5 remove all completed items                         *")
    print("*       6 exit from the program                              *")
    print("*                                                            *")
    print("**************************************************************")


def user_input():
    try:
        user_input = int(input("\033[34m" + "Please choose: " + "\033[39m"))
        if user_input == 1:
            commands.list_item(commands.load())
        elif user_input == 2:
            commands.add_item(commands.load())
        elif user_input == 3:
            commands.list_item(commands.load())
            commands.change_status_item(commands.load())
        elif user_input == 4:
            commands.list_item(commands.load())
            commands.remove_item(commands.load())
        elif user_input == 5:
            commands.remove_completed_items(commands.load())
        elif user_input == 6:
            exit()
        else:
            print("Please choose a number from the menu!")
    except ValueError:
        print("Please enter a number!")

while True:
    print_menu()
    user_input()
