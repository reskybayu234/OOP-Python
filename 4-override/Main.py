class Player:
    def __init__(self,name2):
        self.name = name2

    def getSkill(self):
        print("normal")

class Indonesia(Player):
    def getSkill(self):
        print("cepat")

class Malaysia(Player):
    def getSkill(self):
        print("stamina")

bayu = Indonesia("bayu")
rodih = Malaysia("rodih")

bayu.getSkill()
rodih.getSkill()

print(bayu.name)       
print(rodih.name)