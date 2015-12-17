from random import randint

class Character():
    def __init__(self, name = "", inventory = []):
        self.name = name
        self.inventory = ["", "Sword", "Leather Armor"]

    def random_status(self):
        self.dexterity = randint(1,6) + 6
        self.health = randint(1,6) + randint(1,6) + 12
        self.luck = randint(1,6) + 6
        self.current_health = self.health
        self.current_luck = self.luck

    def reduce_health(self):
        self.current_health = self.health - 2

    def roll(self):
        self.roll_number = randint(1, 6) + randint(1, 6)

    def strike_strength(self):
        self.roll()
        return(self.roll_number + self.dexterity)

    def print_roll_status(self):
        print("dexterity: " + str(self.dexterity) + "\n" + "health: " + str(self.health) + "\n" + "luck: " + str(self.luck))

    def print_inventory_status(self):
        print("inventory: " + self.inventory[0] + ", " + self.inventory[1] + ", " + self.inventory[2])

    def print_start_status_character(self):
        print("Name: " + self.name + "\n" + "Max health: " + str(self.health) + "\n" + "Dexterity: " + str(self.dexterity) + "\n" + "Max luck: " + str(self.luck) + "\n")

    def print_start_status_monster(self):
        print("Monster name: " + self.name + "\n" + "Max health: " + str(self.health) + "\n" + "Max dexterity: " + str(self.dexterity) + "\n")

    def create_dictionary(self):
        dictionary = {'name' : self.name, 'max_dexterity' : self.dexterity, 'current_health': self.current_health, 'max_health' : self.health, 'current_luck': self.current_luck, 'max_luck' : self.luck, 'inventory' : [self.inventory[0], self.inventory[1], self.inventory[2]]}
        return dictionary

class Fight:
    def is_hit(self):
        if user.strike_strength() > monster.strike_strength():
            return True
        elif user.strike_strength() < monster.strike_strength():
            return False
        else:
            return self.is_hit()

    def after_strike(self):
        if self.is_hit():
            monster.reduce_health()
        else:
            user.reduce_health()

    def luck(self):
        if self.is_hit():
            if user.current_luck < user.roll_number:
                monster.current_healt -= 1
            elif user.current_luck >= user.roll_number:
                monster.current_healt -= 4
                user.current_luck -= 1
        else:
            if user.current_luck < user.roll_number:
                user.current_healt -= 3
            elif user.current_luck >= user.roll_number:
                monster.current_healt -= 1
                user.current_luck -= 1


user = Character()
monster = Character()
fight = Fight()
