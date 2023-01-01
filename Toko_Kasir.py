class Toko:

    def menu(self, nama, harga, quantity):
        self.inputnama = nama
        self.inputharga = harga
        self.tquantity = quantity

    def tampil(self):
        pass

class Merk_Dagang(Toko):

    def __init__(self):