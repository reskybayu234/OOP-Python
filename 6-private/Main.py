class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama =nama
        self.__nim = '25'

    def getName(self):
        print(self.nama + self.__nim)

bayu = Mahasiswa("bayu",23)
bayu.nama = "resky"
bayu.__nim = '30'
bayu.getName()