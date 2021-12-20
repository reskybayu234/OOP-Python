class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim

    def getNama(self):
        return self.nama

    def getNim(self):
        return self.nim

class Matkul(Mahasiswa):
    def __init__(self,nama,nim):
        pass
        super().__init__(nama,nim)
        
    def getMatkul(self):
        print("Matematika")


Mahasiswa1 = Matkul("bayu",133)

print(Mahasiswa1.getMatkul())
print(Mahasiswa1.getNama())