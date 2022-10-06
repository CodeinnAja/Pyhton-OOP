class Biodata: # ini class

    def __init__(self, inputNama, inputNim, inputNilai, inputProdi, inputTa): # ini constructor
        self.nama = inputNama
        self.nim = inputNim
        self.nilai = inputNilai
        self.prodi = inputProdi
        self.ta = inputTa

    def data(self): # ini function atau method
        print("==================Biodata Pribadi=============")
        print("Nama Mahasiswa  : " + self.nama)
        print("Nim Mahasiswa   : " + self.nim)
        print("Nilai Mahasiswa : " + str(self.nilai))
        print("Prodi Mahasiswa : " + self.prodi)
        print("Judul Tugas     : " + self.ta)

    def ubah(self):  # tugas ubah nama di properti nama
            print("==================Biodata Pribadi Update=============")
            print("Nama Mahasiswa  : " + self.nama[:0] + "joni ahmad")
            print("Nim Mahasiswa   : " + self.nim)
            print("Nilai Mahasiswa : " + str(self.nilai))
            print("Prodi Mahasiswa : " + self.prodi)
            print("Judul Tugas     : " + self.ta)

    def tambahNilai(self): # tugas tambah nilai di properti nilai
        print("==================Biodata Pribadi Update=============")
        print("Nama Mahasiswa  : " + self.nama)
        print("Nim Mahasiswa   : " + self.nim)
        print("Nilai Mahasiswa : " + str(self.nilai + 29))
        print("Prodi Mahasiswa : " + self.prodi)
        print("Judul Tugas     : " + self.ta)


mahasiswa = Biodata("joko ardiyanto", "c20010007", 86, "Teknik Informatika", "Sistem informasi arsip") # ini objek

mahasiswa.data() # iini untuk menampilkan data
mahasiswa.ubah()
mahasiswa.tambahNilai()