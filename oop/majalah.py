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
