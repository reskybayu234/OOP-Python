class Hero:
    def __init__(self,name,health,attackPower,armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + " diserang " + lawan.name)
        attack_diterima = attackPower_lawan/self.armorNumber
        print("attack diterima : " + str(attack_diterima))
        self.health -= attack_diterima
        print("darah " + self.name + " " + str(self.health))

snipper = Hero("sniper",100,10,10)
ayame = Hero("ayame",80,120,9)

snipper.serang(ayame)
print("\n")
ayame.serang(snipper)