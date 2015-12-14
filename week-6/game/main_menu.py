
class Menu():
    def __init__(self, menu_items):
        self.menu_items = menu_items.split(",")

    def list_menu(self):
        output = ""
        i = 1
        for item in range(len(self.menu_items)):
            output += str(i) + " " + self.menu_items[item] + "\n"
            i += 1
        return output

    def user_input(self):
        try:
            user_input = int(input("Please choose a number from the menu: "))
            if not user_input or user_input > len(self.menu_items):
                raise ValueError
        except ValueError:
            print("You entered a wrong number! Please choose a new one from the menu! ")
            self.user_input()
        return user_input

    # def print_menu(self):
    #     print(self.list_menu())
    #     self.user_input()
