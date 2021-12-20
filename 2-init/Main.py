class Main:
    name = ''
    speed = ''

    def __init__(self,name2,speed2):
        self.name = name2
        self.speed = speed2


    def getName(self):
        return self.name
    
    def getSpeed(self):
        return self.speed

    def fung(self):
        print("hallo nama saya " + self.name)

bayu = Main("bayu",99)
# fais = Main("fais",55)

# print(bayu.getName())
# print(bayu.getSpeed())

bayu.fung()
# print(fais)