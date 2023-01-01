from store import  Toko
from novel import Novel
from komik import Komik
from majalah import Majalah

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