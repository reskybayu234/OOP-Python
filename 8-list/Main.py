Barang = ["kunci","ember","jaket","ban","mobil","mobil"]
print(type(Barang))

Barang.append("bantal")
print(Barang)

data = "test"
for i in data:
    print(i)

Barang.extend("baju")
print(Barang)

Barang.insert(3,"monitor")
print(Barang)

# method untuk menghitung jumlah anggota
jumlahSepeda = Barang.count("mobil")
print(jumlahSepeda)

stuff = Barang.copy()
stuff.append("kursi")
print(stuff)
print(Barang)