class Hero:
    __jumlah = 0

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    def getJumlah(self): # hanya untuk objek
        return Hero.__jumlah

    def getJumlah1(): # hanya berlaku untuk class
        return Hero.__jumlah

    @staticmethod 
    def getJumlah2(): # berlaku untuk objek dan class
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
snipper = Hero("snipper")
print(snipper.getJumlah3())