from random import randint

class Character():
    def __init__(self, name = ""):
        self.name = name
        self.random_status()
        self.inventory = inventory

    def random_status(self):
        self.dexterity += randint(1,6) + 6
        self.health += 2 * randint(1,6) + 6
        self.luck += randint(1,6) + 6
