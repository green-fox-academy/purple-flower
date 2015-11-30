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

    def strike(self,ennemy):
        ennemy.HP -= self.damage
        print("Ennemy HP: " + str(ennemy.HP))

class Cerlic(GameCharacter):
    def heal(self, ally):
        ally.HP += 10
        print("Ally HP:" + str(ally.HP))

goodguy = GameCharacter("Goodguy", 100, 40)
badguy = GameCharacter("Badguy", 100, 45)
melkor = Cerlic("Melkor", 1000, 80)

goodguy.drink_potion()
for i in range(2):
    goodguy.strike(badguy)
    melkor.heal(badguy)

goodguy.print_status()
badguy.print_status()
