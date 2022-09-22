class Hero:
    def __init__(self, inputName, inputHp, inputArmor):
        self.name = inputName
        self.hp = inputHp
        self.armor = inputArmor


hero1 = Hero("Natalia", 100, 80)
hero2 = Hero("Balerick", 155, 200)

print(hero1.name)
print(hero1.armor)

print(hero2.__dict__)

