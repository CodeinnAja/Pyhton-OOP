class Biodata: # ini class


    def data(self): # ini function atau method
        print("==================Biodata Pribadi=============")
        print("Nama Mahasiswa  : " + self.nama)
        print("Nim Mahasiswa   : " + self.nim)
        print("Nilai Mahasiswa : " + str(self.nilai))
        print("Prodi Mahasiswa : " + self.prodi)
        print("Judul Tugas     : " + self.ta)


mahasiswa = Biodata() # ini objek

mahasiswa.nama = "Joko Ardiyanto"
mahasiswa.nim = "C20010007"
mahasiswa.nilai = 86
mahasiswa.prodi = "Teknik Informatika"
mahasiswa.ta = "sistem informasi arsip"

mahasiswa.data()