class Biodata:

    def __init__(self, inputNama, inputNim, inputNilai, inputProdi, inputaddr):
        self.nama = inputNama
        self.nim = inputNim
        self.nilai = inputNilai
        self.prodi = inputProdi
        self.addr = inputaddr

    def tampil(self): # ini function atau method
        print("==================Biodata Pribadi=============")
        print("Nama Mahasiswa  : " + self.nama)
        print("Nim Mahasiswa   : " + self.nim)
        print("Nilai Mahasiswa : " + str(self.nilai))
        print("Prodi Mahasiswa : " + self.prodi)
        print("alamat     : " + self.addr)

data1 = Biodata("joko ardiyanto", "c20010007", 86, "Teknik Informatika", "dk.nenden, ampel")

data1.tampil()
