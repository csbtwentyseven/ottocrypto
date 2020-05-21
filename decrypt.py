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


    def oeSade(hash):
        parcailk = hash[16:len(hash)-17]
        parcasade = parcailk[:int(len(parcailk) / 2)] #hash'ı fazlalıklardan arındırıyoruz
        duz_harfler = list()

        j = 0#döngü index degiskeni
        tc = 0#ilk durak tespit degiskeni

        print(parcasade)


        for i in parcasade: #eğer tek haneli (Q Sayisi) ise bu şekilde ekliyor.
            if(i == "Q"):
                duz_harfler.append(parcasade[j+1])

            elif((i == "T" or i == "C")):#durak tespti
                if(tc == 0):#ilk durak tespiti
                    print(parcasade[j-2] + parcasade[j-1])
                    tc = 1

                print(parcasade[j+3]+parcasade[j+4]) #ilk durağın hem solu hem sağında şifreler var.bunları else alma sağındaki şifreler çekilmiyor.


            j = j + 1



        return parcasade






def main():
    if(Kir.modCek(csb) == "oe"):
        Kir.oeSade(csb)

    elif(Kir.modCek(csb) == "oa"):
        Kir.Oa(csb)

if __name__ == '__main__':
    main()