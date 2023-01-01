class Kasir:
    nopesanan = 0
    hargaTotal = 0
    hargaTambahan = 0
    hargabayar = 0
    def __init__(self, inputnama, inputjml, inputharga):
        self.nama = inputnama
        self.jumlah = inputjml
        self.harga = inputharga

        Kasir.nopesanan += 1
        Kasir.hargaTotal = self.jumlah * self.harga
        Kasir.hargaTambahan = DataTransaksi.jumlah * DataTransaksi.harga
        Kasir.hargabayar = Kasir.hargaTotal + Kasir.hargaTambahan

    def tampil(self):
        print("=============================")
        print("pesanan no ", Kasir.nopesanan)
        print("Nama pesanan ", self.nama)
        print("jumlah pesanan ", self.jumlah)
        print("harga   ", self.harga)
        print("Total Harga Pesanan : ", Kasir.hargaTotal)

    def total(self):
        print("Harga bayar : ", Kasir.hargabayar)

class DataTransaksi(Kasir):

        tambahan1 = input("tambahan laku : ")
        jumlah = int(input("jumlah : "))
        harga = int(input("harga : "))

        def tampiltambahan(self):
            print("tambahan  : ", DataTransaksi.tambahan1)
            print("jumlah    : ",DataTransaksi.jumlah)
            print("Harga     : ",DataTransaksi.harga)
            print("harga total tambahan ", DataTransaksi.hargaTambahan)


transaksi1 = DataTransaksi(input("nama pesanan "), int(input("jumlah pesanan ")), int(input("Harga ")))

transaksi1.tampil()
transaksi1.tampiltambahan()
transaksi1.total()