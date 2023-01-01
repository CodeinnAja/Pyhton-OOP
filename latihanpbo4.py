class Sosmed:
    no=0

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
        #print("No Telp Nasabah     : ", EditData.telpon(self))

        print("\n======================\n")

    def EditPass(self): #Setter
        self.__passwd = input("Masukkan Password Anda : ")


#class EditData(Sosmed):
   # __NoTelp="08123323232334"

    #def telpon(self): #Getter
    #    return self.__NoTelp


class Update(Sosmed):
    pass


akun1 = Update(input("Masukkan Username : "), input("Masukkan Email : "),
int(input("Masukkan password : ")), input("Masukan hobi : "))
akun1.EditPass()

akun1.tampil()
