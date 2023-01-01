# membuat sebuah multiple inheritance (overide method)

class Toko:

    def __init__(self, inputJudul, inputJenis):
        self.judul = inputJudul
        self.jenis = inputJenis

    def judul_program(self):
        print("Toko Buku".center(30, "=")+("\n"))

        print("1. Komik")
        print("2. Novel")
        print("3. Majalah")

        print(30*"=")

class Komik:

    def harga_komik(self):
        print("1. Harga komik naruto    Rp.30.000")
        print("2. Harga komik bleach    Rp.40.000")
        print("3. Harga komik one piece Rp.45.000 \n")

    def pembelian_komik(self):
            pilihan = input("Choose ? ")
            jumlah = int(input("Masukan jumlah pembelian anda : "))
            if pilihan == "1":
                harga = jumlah*30000
                print(f"anda membeli {jumlah} Komik \n"+ f"dengn total harga {harga}")
            elif pilihan == "2":
                harga = jumlah*40000
                print(f"anda membeli {jumlah} Komik \n" + f"dengn total harga {harga}")
            elif pilihan == "3":
                harga = jumlah * 50000
                print(f"anda membeli {jumlah} Komik \n" + f"dengn total harga {harga}")
            else: quit("input salah !!")


class Novel:
    def harga_novel(self):
        print("1. Harga novel dia          Rp.90.000")
        print("2. Harga novel first love   Rp.68.000")
        print("3. Harga novel dadi payung  Rp.75.000 \n")

    def pembelian_novel(self):
            pilihan = input("Choose ? ")
            jumlah = int(input("Masukan jumlah pembelian anda : "))
            if pilihan == "1":
                harga = jumlah*90000
                print(f"anda membeli {jumlah} Novel dia \n"+ f"dengn total harga {harga}")
            elif pilihan == "2":
                harga = jumlah*68000
                print(f"anda membeli {jumlah} Novel first love \n" + f"dengn total harga {harga}")
            elif pilihan == "3":
                harga = jumlah * 75000
                print(f"anda membeli {jumlah} Novel payung \n" + f"dengn total harga {harga}")
            else: quit("input salah !!")

class Majalah:
    def harga_majalah(self):
        print("1. Harga majalah warta       Rp.10.000")
        print("2. Harga majalah life style  Rp.32.000")
        print("3. Harga majalah seni        Rp.11.000 \n")

    def pembelian_majalah(self):
            pilihan = input("Choose ? ")
            jumlah = int(input("Masukan jumlah pembelian anda : "))
            if pilihan == "1":
                harga = jumlah*10000
                print(f"anda membeli {jumlah} Majalah warta \n"+ f"dengn total harga {harga}")
            elif pilihan == "2":
                harga = jumlah*32000
                print(f"anda membeli {jumlah} Majalah life style \n" + f"dengn total harga {harga}")
            elif pilihan == "3":
                harga = jumlah * 11000
                print(f"anda membeli {jumlah} Majalah seni \n" + f"dengn total harga {harga}")
            else: quit("input salah !!")


class Pembelian(Toko,Komik,Novel,Majalah):
    def beli(self):
        if self.jenis == "1" :
            self.harga_komik()
            self.pembelian_komik()
        elif self.jenis == "2":
            self.harga_novel()
            self.pembelian_novel()
        elif self.jenis == "3" :
            self.harga_majalah()
            self.pembelian_majalah()
        else: quit("input salah")



pembeliaan1 = Pembelian(Toko.judul_program(self=Toko),
                        input("Masukan jenis pembelian yang akan dibeli : "))

pembeliaan1.beli()