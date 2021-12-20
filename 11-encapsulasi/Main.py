class Hero:
    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower

    # getter
    def getName(self):
        return self.__name

    # setter
    def diserang(self,attack_lawan):
        self.__health -= attack_lawan

    def setAttack(self,attack_baru):
        self.__attackPower = attack_baru

earthshaker = Hero("earthshaker",100,50)
snipper = Hero("snipper",100,80)

# print(earthshaker.getName())

print(earthshaker.setAttack(5))
print(earthshaker.__dict__)