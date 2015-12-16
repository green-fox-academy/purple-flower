class Menu:
    def __init__(self, items):
        self.items = items

    def list_menu(self):
        output= ""
        for item in self.items:
            output += str(item.num) + " " + item.name + "\n"
        return output

    def ask_user_input(self):
        while True:
            try:
                user_input = int(input("Please choose a number from the menu: "))
                if not user_input or user_input > len(self.items):
                    raise ValueError
                return user_input
            except ValueError:
                print("You entered a wrong number! Please choose a new one from the menu! ")


    def choose(self):
        input_received = self.ask_user_input()
        for item in self.items:
            if item.num == input_received:
                return item.action()

    def selected_item_name(self):
        selected_item = self.ask_user_input()
        for item in self.items:
            if item.num == selected_item:
                return item.action

    def display_menu(self):
        print(self.list_menu())
        self.choose()
