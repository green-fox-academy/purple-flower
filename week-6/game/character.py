from random import randint

class Character():
    def __init__(self, name = "", inventory = []):
        self.name = name
        self.random_status()
        self.inventory = ["", "Sword", "Leather Armor"]

    def random_status(self):
        self.dexterity = randint(1,6) + 6
        self.health = 2 * randint(1,6) + 12
        self.luck = randint(1,6) + 6

    def strike(self):
        self.current_health = self.health - 2

    def roll(self):
        self.roll_number = 2 * randint(1, 6)

    def strike_strength(self):
        self.roll()
        return(self.roll_number + self.dexterity)

    def print_roll_status(self):
        print("dexterity: " + str(self.dexterity) + "\n" + "health: " + str(self.health) + "\n" + "luck: " + str(self.luck))

    def print_inventory_status(self):
        print("inventory: " + self.inventory[0] + ", " + self.inventory[1] + ", " + self.inventory[2])

    def print_start_status_character(self):
        print("Name: " + self.name + "\n" + "Max health: " + str(self.health) + "\n" + "Max dexterity: " + str(self.dexterity) + "\n" + "Max luck: " + str(self.luck) + "\n")

    def print_start_status_monster(self):
        print("Monster name: " + self.name + "\n" + "Max health: " + str(self.health) + "\n" + "Max dexterity: " + str(self.dexterity) + "\n")

    def create_dictionary(self):
        dictionary = {'name' : self.name, 'max_dexterity' : self.dexterity, 'max_health' : self.health, 'max_luck' : self.luck, 'inventory' : [self.inventory[0], self.inventory[1], self.inventory[2]]}
        return dictionary
