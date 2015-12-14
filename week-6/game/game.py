import main_menu

main_menu_items = main_menu.Menu("New Game,Load Game,Exit")
submenu_items = main_menu.Menu("Reenter name,Continue,Save,Quit")

print(main_menu_items.list_menu())

while True:
    selected_number_by_user = main_menu_items.user_input()

    if selected_number_by_user == 1:
        name = input("Please enter your name: ")
        print("Your character name is " + name + ".")
        print(submenu_items.list_menu())
        selected_submenu_by_user = submenu_items.user_input()

    elif selected_number_by_user == 2:
        pass
    elif selected_number_by_user == 3:
        exit()
