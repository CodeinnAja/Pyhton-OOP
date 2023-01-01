class Hero:

    jumlah = 0 # class variabel

    def __init__(self, inputName, inputHp, inputArmor):
        #instance variabel
        self.name = inputName
        self.hp = inputHp
        self.armor = inputArmor
        Hero.jumlah += 1

    #void function, di py method tanpa return
    def panggil(self):
        print("hai namaku adalah ", self.name)


    #method dng argumen tanpa return
    def tambahDarah(self,up):
        self.hp += up

    #method dng return
    def getHealt(self):
        return self.hp


hero1 = Hero("Natalia", 100, 80)
hero2 = Hero("Balerick", 155, 200)

print(hero1.hp)

hero1.panggil()
hero1.tambahDarah(10)
print(hero1.getHealt())
