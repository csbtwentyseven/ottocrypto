import random
csb = input("Lütfen Şifrelemek İstediğiniz Metni Giriniz: ")


class ModAyar():

    def modDegis(encryptionMod): # sifreleme modunu kelime uzunluguna gore belirler
        dosya = open('mod.txt', 'w')
        dosya.write(encryptionMod)

    def modCek(): # sifreleme modunu her cagrildiginda geri dondurur.
        dosya = open('mod.txt', 'r')
        for satir in dosya:
            return satir

class Sezar():
     latin_tablo = {"a":21,
                    "b":2,
                    "c":6,
                    "ç":7,
                    "d":10,
                    "e":1,
                    "f":23,
                    "g":26,
                    "ğ":22,
                    "h":8,
                    "ı":37,
                    "i":38,
                    "j":14,
                    "k":24,
                    "l":28,
                    "m":29,
                    "n":27,
                    "o":39,
                    "ö":40,
                    "p":3,
                    "r":12,
                    "s":5,
                    "ş":16,
                    "t":4,
                    "u":39,
                    "ü":40,
                    "v":31,
                    "y":36,
                    "z":11,
                    } #latin - osmanlı alfabe karşılığı

     def latinDeger(harf): #latince ifadenin sayısal karşılığını
         if(len(harf) != 1):
             return "lütfen bir harf giriniz!"
         else:
             return Sezar.latin_tablo.get(harf)

class Incele():
    basla = 0
    bitir = 1
    harfler = list()

    def durak():
        durak = ["T","C"]
        durakEkle = random.sample(durak,1) #durak aralarına rastgele t ya da c harflerinden birini ekler.
        return durakEkle

    def parcala(): #string parçalandı harfler isimli bir listeye tüm harfleri tek tek atıldı.
        for i in range(0,len(csb)):
            Incele.harfler.append(csb[Incele.basla+i:Incele.bitir+i])
            Incele.harfler = Incele.harfler + Incele.durak()

        print(Incele.harfler)
        return Incele.harfler






def main():
    if(len(csb) % 2 == 0): #kelime uzunluguna gore mod verisi gonderir
        ModAyar.modDegis("oe")
    else:
        ModAyar.modDegis("oa")

    Incele.parcala()




if __name__ == '__main__':
    main()
