class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def info(self):
        print("{} dengan health : {}".format(self.name,self.health))

class Hero_Strength(Hero):
    def __init__(self,name,health):
        super().__init__(name,health)
        super().info()

class Hero_Intelligent(Hero):
    def __init__(self,name,health):
        super().__init__(name,health)
        super().info()

# membuat objek bayu dan suep
bayu = Hero_Strength("bayu",100)
suep = Hero_Intelligent("suep",200)
