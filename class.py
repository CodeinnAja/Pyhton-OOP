class Hero:  # ini class header
    pass


hero1 = Hero()  # ini object
hero2 = Hero()

hero1.name = "Natalia"
hero1.hp = 100

hero2.name = "Rafaela"
hero2.hp = 120

print(hero1.__dict__)
print(hero2.name)
print(hero2.hp)
