from store import Toko
from pembelian import Pembelian

pembeliaan1 = Pembelian(Toko.judul_program(self=Toko),
                        input("Masukan jenis pembelian yang akan dibeli : "))
print("\n")
pembeliaan1.beli()
print("Transaksi Berhasil \n")

while True:
    answer = input("Tambah Transaksi Pembelian (Y/N) ? ")
    if(answer == "Y" or answer == "y"):
        pembeliaan1 = Pembelian(Toko.judul_program(self=Toko),
                                input("Masukan jenis pembelian yang akan dibeli : "))
        print("\n")
        pembeliaan1.beli()
        print("Transaksi Berhasil \n")

    else:
        quit("Terimakasih Atas Pembeliannya")
