import commands



def print_menu():
    print("*****************************************************************")
    print("*                           MENU                                *")
    print("*                                                               *")
    print("*       1 list items                                            *")
    print("*       2 add item                                              *")
    print("*       3 change item status                                    *")
    print("*       4 remove item from the list                             *")
    print("*       5 exit from the program                                 *")
    print("*                                                               *")
    print("*                                                               *")
    print("*****************************************************************")


def user_input():
    try:
        user_input = int(input("Please choose: "))
        if user_input == 1:
            commands.list_item(commands.load())
        elif user_input == 2:
            commands.add_item(commands.load())
        elif user_input == 3:
            commands.list_item(commands.load())
            commands.complete_item(commands.load())
        elif user_input == 4:
            commands.list_item(commands.load())
            commands.remove_item(commands.load())
        elif user_input == 5:
            exit()
    except ValueError:
        print("Please enter a number!")

while True:
    print_menu()
    user_input()
