class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

class Hero_Strength(Hero):
    pass

bayu = Hero("bayu",100)
ayip = Hero_Strength("ayip",20)
# print(bayu.name)
print(ayip.__dict__)

