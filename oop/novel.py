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
