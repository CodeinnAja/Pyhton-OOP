class Hero:

    def __init__(self, name, health, attackPower, armor):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor

    def serang(self):
        print(self.name + "Menyerang")
