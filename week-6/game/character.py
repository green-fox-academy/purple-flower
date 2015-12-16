from random import randint

class Character():
    def __init__(self, name = "", inventory = []):
        self.name = name
        self.random_status()
        self.inventory = ["", "Sword", "Leather Armor"]

    def random_status(self):
        self.dexterity = randint(1,6) + 6
        self.health = 2 * randint(1,6) + 6
        self.luck = randint(1,6) + 6

    def print_roll_status(self):
        print("dexterity: " + str(self.dexterity) + "\n" + "health: " + str(self.health) + "\n" + "luck: " + str(self.luck))

    def print_character_status(self):
        self.print_roll_status
