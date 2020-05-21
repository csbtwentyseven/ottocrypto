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
        j = 0

        print(parcasade)


        for i in parcasade: #eğer tek haneli (Q Sayisi) ise bu şekilde ekliyor.
            if(i == "Q"):
                duz_harfler.append(parcasade[j+1])

            if (j == 3 and (i == "T" or i == "C")):
                print("j=", j)
                print(parcasade[1] + parcasade[2])
            elif (j == 2 and (i == "T" or i == "C")):
                print("j=", j)
                print(parcasade[0] + parcasade[1])

            elif((i == "T" or i == "C")):#cift haneli sifrelerin tespit ve listeye eklenmesi
                print(parcasade[j+3]+parcasade[j+4])


            j = j + 1



        return parcasade






def main():
    if(Kir.modCek(csb) == "oe"):
        Kir.oeSade(csb)

    elif(Kir.modCek(csb) == "oa"):
        Kir.Oa(csb)

if __name__ == '__main__':
    main()