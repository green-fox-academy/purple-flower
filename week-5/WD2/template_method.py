class Weapon:
    def strike(self, opponent):
        self.damage()
        self.self_damage()

    def damage(self):
        pass

    def damage_opponent(self, opponent):
        pass

    def self_damage(self):
        pass

class Sword(Weapon):
    def damage(self):
        return 20

    def damage_ooponent(self, opponent):
        opponent.hp -= self.damage

    def self_damage(self):
        self.hp -= self.damage * 0.1


class MagicWand(Weapon):
    def damage(self):
        return 15

    def damage_opponent(self, opponent):
        opponent.hp -= self.damage

    def self_damage(self):
        self.hp -= self.damage * 0.1

class Musket(Weapon):
    def damage(self):
        return 30

    def damage_opponent(self, opponent):
        opponent.hp -= self.damage

    def self_damage(self):
        self.hp -= self.damage * 0.1

class Warrior:
    def __init__(self, weapon):
        self.hp = 100
        self.weapon = weapon

    def strike(self, opponent):
