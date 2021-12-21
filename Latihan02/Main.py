class Hero:
    __jumlah = 0

    def __init__(self,name,health,attackPower,armor):
        self.__name = name
        self.__healthStandar = health
        self.__attackPowerStandar = attackPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attackPower = self.__attackPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level = {} : \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attackPower,self.__armor)

    @property      
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if self.__exp >= 100:
            print(self.__name, "level up")
            self.__level += 1
            self.__exp += 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attackPower = self.__attackPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def serang(self,musuh):
            self.gainExp = 50

slardar = Hero("slardar",100,5,10)
maxi = Hero("maxi",100,30,50)

slardar.serang(maxi)
slardar.serang(maxi)
slardar.serang(maxi)

print(slardar.info)