class GameCharacter():
    def __init__(self, name, HP, damage):
        self.name = name
        self.HP = HP
        self.damage = damage

    def print_status(self):
        if self.HP <= 0:
            print("This character, ")
            print(self.name)
            print("is dead.")
        else:
            print(self.name)
            print("HP: " + str(self.HP))

    def drink_potion(self):
        self.HP += 10

    def strike(self,other):
        other.HP -= self.damage

goodguy = GameCharacter("goodguy", 100, 40)

badguy = GameCharacter("badguy", 100, 45)

goodguy.drink_potion()
goodguy.strike(badguy)

goodguy.print_status()
badguy.print_status()
