class Toko_Buku:
    no_buku = 0
    t_harga = 0 # variabel class
    total_fix = 0

    def __init__(self, inputJudul, inputJumlah, inputHarga):
        self.judul = inputJudul
        self.jumlah = inputJumlah # instance variabel
        self.harga = inputHarga

        Toko_Buku.no_buku += 1
        Toko_Buku.show(self)
        Toko_Buku.t_harga = inputJumlah*inputHarga # dari tanda += dihilangkan jadi =
        Toko_Buku.diskon(self, diskon_harga=40000)
        print("Total Harga : ", Toko_Buku.hargaToatal(self))


    def show(self): # method tanpa argumen
        print(30*"=")
        print("Buku nomer  : ", Toko_Buku.no_buku)
        print("Judul Buku  : ", self.judul)
        print("Jumlah Buku : ", self.jumlah)
        print("Harga Buku  : ", self.harga)

    def diskon(self, diskon_harga): # method dengan argumen
        Toko_Buku.t_harga -= diskon_harga
        #print(30*"=")
        print("DISKON      : ", diskon_harga)

    def hargaToatal(self): # method dengan return
        return Toko_Buku.t_harga


buku1 = Toko_Buku("Laskar Pelangi", 2, 50000)
buku2 = Toko_Buku("Harry potter", 2, 25000)
#buku1.show()
#buku2.show()
#buku1.diskon(40000)
#print("Total Bayar : ", Toko_Buku.t_harga)
print(30*"=")
print("Jumlah Pembayaran  : Rp.", Toko_Buku.total_fix)