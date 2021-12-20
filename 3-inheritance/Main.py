class Mobil:
    def __init__(self,nama):
        self.name = nama

    def printNama(self):
         print("method printNama")

    def printJenis(self):
         print("method printJenis")

class Jok(Mobil):
    pass


warna = Jok("bayu")
warna.printJenis()