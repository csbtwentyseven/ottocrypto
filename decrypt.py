csb = input("Lütfen Kırmak İstediğiniz Şifreyi Yazınız:")


class Kir():
    def modCek(hash): #Modu tespit edip gönderir.
        if(hash != ""):
            if(hash[2] == "."):
                return "oe"
            else:
                return "oa"
        else:
            print("Lütfen bir hash giriniz!")


    def oeSade(hash): # oe modunu sadeleştirir.
        dosya = open('parcasade.txt', 'w')

        parcailk = hash[16:len(hash)-17]
        parcasade = parcailk[:int(len(parcailk) / 2)] #hash'ı fazlalıklardan arındırıyoruz

        dosya.write(parcasade)
        dosya.close()
        Kir.decode()

    def oAsade(self): #oa modunu sadeleştirir.
        pass


    def decode(): #gelen sade hash'in sayisal verilerini ayıklar.
        dosyaYaz = open('decrypt.txt', 'w')
        dosyaOku = open('parcasade.txt', 'r')
        parcasade = dosyaOku.read()

        j = 0  # döngü index degiskeni
        tc = 0  # ilk durak tespit degiskeni
        print(parcasade)
        for i in parcasade:
            if((i == "T" or i == "C")):#durak tespti

                if(tc == 0):#ilk durak tespiti
                    dosyaYaz.write(parcasade[j-2] + parcasade[j-1]) # ilk durağın solundaki iki sayıyı yazıyor.
                    tc = 1 # ilk duraktan sonra degiskeni degistirerek ilk duragı isaretliyor.
                try:
                    dosyaYaz.write(parcasade[j+3]+parcasade[j+4]) #durakların iki index sağındaki harfleri dosyaya yazıyor.bkz:encrypt.py
                except:
                    pass
            j = j + 1

        dosyaOku.close()
        dosyaYaz.close()
        Eslestir.sayidanharf()

class Eslestir():
    def sayidanharf():
        sayisalTM = open('decrypt.txt', 'r').read() # sayisalTM = Sayısal Temiz Metin
        j = 0 #döngü index degiskeni
        for i in sayisalTM:
            if(j%2 == 0):
                print(sayisalTM[j] + sayisalTM[j+1])
            j = j+1







def main():
    if(Kir.modCek(csb) == "oe"):
        Kir.oeSade(csb)

    elif(Kir.modCek(csb) == "oa"):
        Kir.oASade(csb)

if __name__ == '__main__':
    main()