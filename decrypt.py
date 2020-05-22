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
        dosyaoe = open('parcasade.txt', 'w')

        parcailk = hash[16:len(hash)-17]
        parcasade = parcailk[:int(len(parcailk) / 2)] #hash'ı fazlalıklardan arındırıyoruz

        dosyaoe.write(parcasade)
        dosyaoe.close()
        Kir.decode()

    def oaSade(self): #oa modunu sadeleştirir.
        print("Sa")


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
    osman_tablo = {"21": "a",
                   "Q2": "b",
                   "Q6": "c",
                   "Q7": "ç",
                   "10": "d",
                   "Q1": "e",
                   "23": "f",
                   "26": "g",
                   "22": "ğ",
                   "Q8": "h",
                   "37": "ı",
                   "38": "i",
                   "14": "j",
                   "24": "k",
                   "28": "l",
                   "29": "m",
                   "27": "n",
                   "39": "o",
                   "40": "ö",
                   "Q3": "p",
                   "12": "r",
                   "Q5": "s",
                   "16": "ş",
                   "Q4": "t",
                   "41": "u",
                   "42": "ü",
                   "31": "v",
                   "36": "y",
                   "11": "z",
                   "T": "T",
                   "C": "C",
                   "1453": " ",
                   }  # latin - osmanlı alfabe karşılığı

    def sayidanharf():
        sayisalTM = open('decrypt.txt', 'r').read() # sayisalTM = Sayısal Temiz Metin
        j = 0 #döngü index degiskeni
        sozelTM = list() #sozelTM = Sözel Temiz Metin
        for i in sayisalTM:
            if(j%2 == 0):
                sozelTM.append(Eslestir.osman_tablo[sayisalTM[j] + sayisalTM[j+1]]) #sayilari harflerle eslestirip sozelTM listesine sırasıyla ekliyoruz
            j = j+1 # index arttır.

            temiz_metin = ''.join(map(str, sozelTM)) #sozelTM listemizi stringe ceviriyoruz.
        print(temiz_metin)





def main():
    if(Kir.modCek(csb) == "oe"):
        Kir.oeSade(csb)

    elif(Kir.modCek(csb) == "oa"):
        Kir.oaSade(csb)

if __name__ == '__main__':
    main()