class Warung:
    jumlah = 0
    t_harga = 0
    def __init__(self, inputNama, inputAdd, inputharga):
        self.nama = inputNama
        self.addr = inputAdd
        self.harga = inputharga

        Warung.t_harga =  inputharga
        pembayaran.bayar(self, uang=5000)

    def identitas(self):

        print("Nama  : ", self.nama)
        print("Alamat :", self.addr)
        print("Harga : ", self.harga)

class Warungt1(Warung):
     print("================Totalan Pembelian==================")
     nama = input("Masukan Menu : ")
     jml = input("masukan jumlah :")
     print("===========Customer Chek list=============")
     def menu1(self):
         print("Menu : ", self.nama)
         print("jumlah beli : ", self.jml)


class pembayaran(Warung):
    uang = 0

    def bayar(self, uang):
        Warung.t_harga -= int(uang)

        print("Harga bayar : ", uang)


    def total(self):
        return  Warung.t_harga


warungA = Warungt1(input("Masukan Nama : "), input("Masukan Alamat : "), input("Masukan Harga :"))

warungA.identitas()
warungA.menu1()
warungA = pembayaran("total : ", pembayaran.total(self=5000))