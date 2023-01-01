class Nasabah :
    nonasahabah = 0

    def __init__(self, name, norekening, pin, saldo):
        self.name = name
        self.norekening = norekening
        self.__pin = pin  # bersifat privat
        self.__saldo = saldo


    def tampil(self):
        print("==============DATA NASABAH=============")
        print("Nama Nasabah  : ", self.name)
        print("No Rekening   : ", self.norekening)
        print("Pin Nasabah   : ", self.__pin)
        print("Saldo Nasabah : ", self.__saldo)

    # membuat sesuatu yang bersifat privat
    def Editpin(self):
        self.__pin = input("Masukan PIN : ")

    def EditSaldo(self):
        self.__saldo = input("Masukan Saldo : ")


class EditNama(Nasabah):
    def editnama(self):
        self.name = input("Masukan nama anda : ")

class Penarikan(Nasabah):
    pass


nasabah1 = Penarikan(input("Input nama anda : "), input("Input No rekening anda :"), input("Input Pin anda :"), int(input("Input saldo anda :")))

nasabah1.editnama()

nasabah1.tampil()