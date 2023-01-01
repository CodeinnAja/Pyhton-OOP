class Sosmed:


    def __init__(self, inputUsername, inputEmail, inputPass, inputHobi):
        self.nama = inputUsername
        self.email = inputEmail
        self.__passwd = inputPass
        self.hobi = inputHobi

    def tampil(self): #Getter
        print("\n=====Data Akun=====\n")
        print("User name        : ", self.nama)
        print("Email anda       : ", self.email)
        print("Password anda    : ", self.__passwd)
        print("kegemaran        : ", self.hobi)

        print("\n======================\n")

    def GetEdit(self):
        self.__passwd = Update.EditPass(self)

class Update(Sosmed):

    def EditPass(self, newPass): #Setter
        self.newPass = input("Masukkan Password Baru : ")


akun1 = Update(input("Masukkan Username : "), input("Masukkan Email : "),
int(input("Masukkan password : ")), input("Masukan hobi : "))
akun1.EditPass()

akun1.tampil()
