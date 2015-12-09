class Sword:
    def damage(self):
        return 10

class MagicWand:
    def damage(self):
        return 20

class Enhanced: #fegyver módosítása dekorátorral
    def __init__(self, weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() + 5

class Rusty:
    def __init__(self, weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() / 2

class Magical:
    def __init__(self, weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() * 2

class Warrior:
    def __init__(self, weapon):
        self.hp = 100
        self.weapon = weapon

    def strike(self, opponent):
        damage = self.weapon.damage()
        opponent.hp -= damage


warrior = Warrior(Magical(Enhanced(Sword())))
opponent = Warrior(Sword())

print(opponent.hp)
warrior.strike(opponent)
print(opponent.hp)

# warrior2 = Warrior(Magical(Enhanced(MagicWand())))
# opponent2 = Warrior(MagicWand())
#
# print(opponent2.hp)
# warrior2.strike(opponent2)
# print(opponent2.hp)
