csb = input("Lütfen Kırmak İstediğiniz Şifreyi Yazınız:")


class Kir():
    def modCek(hash):
        if(hash != ""):
            if(hash[2] == "."):
                return "oe"
            else:
                return "oa"
        else:
            print("Lütfen bir hash giriniz!")

    def Oe_p(hash):
        parcailk = hash[17:len(hash)-17]
        parcason = parcailk[:int(len(parcailk) / 2)] #hash'ı fazlalıklardan arındırıyoruz

        print(parcason)

        return parcason




def main():
    if(Kir.modCek(csb) == "oe"):
        Kir.Oe_p(csb)

    elif(Kir.modCek(csb) == "oa"):
        Kir.Oa(csb)

if __name__ == '__main__':
    main()