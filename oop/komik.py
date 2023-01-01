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
