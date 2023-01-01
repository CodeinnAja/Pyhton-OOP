class Buku: # class  ini materi inheritence
    jumlah = 0

    def __init__(self, inputJenis, inputStok):  # construktor
        self.jenis = inputJenis
        self.stok = inputStok

    def keterangan(self):  # method
        print(30*"=")
        print("Jenis Buku : ", self.jenis)
        print("Stok Buku  : ", self.stok)


class Buku_Turunan(Buku):  # class child
    judul = input("Masukan judul   : ")
    harga = input("Masukan harga   : ")
    author = input("Masukan author : ")

    def data_buku(self):
        print(30*"=")
        print("Judul buku : ", self.judul)
        print("Harga buku : ", self.harga)
        print("Pengarang  : ", self.author)

# object
#buku1 = Buku(input("Masukan jenis buku : "), input("Masukan stock buku :"))
buku2 = Buku_Turunan(input("Masukan jenis buku : "), input("Masukan stock buku :"))

#buku1.keterangan()
buku2.data_buku()
buku2.keterangan()