# © CARULLAH SAİD BERK
import random
metin = input("Lütfen Şifrelemek İstediğiniz Metni Giriniz: ")
csb = metin.lower()  # inputu alıp küçük harflere döküyoruz.

class ModAyar():

    def modDegis(encryptionMod): # sifreleme modunu kelime uzunluguna gore belirler
        dosya = open('mod.txt', 'w')
        dosya.write(encryptionMod)

    def modCek(): # sifreleme modunu her cagrildiginda geri dondurur.
        dosya = open('mod.txt', 'r')
        for satir in dosya:
            return satir

class Sezar():
     latin_tablo = {"a":"21",
                    "b":"Q2",
                    "c":"Q6",
                    "ç":"Q7",
                    "d":10,
                    "e":"Q1",
                    "f":23,
                    "g":26,
                    "ğ":22,
                    "h":"Q8",
                    "ı":37,
                    "i":38,
                    "j":97,
                    "k":24,
                    "l":28,
                    "m":29,
                    "n":27,
                    "o":39,
                    "ö":40,
                    "p":"Q3",
                    "r":12,
                    "s":"Q5",
                    "ş":16,
                    "t":"Q4",
                    "u":41,
                    "ü":42,
                    "v":31,
                    "y":36,
                    "z":11,
                    "T":"T",
                    "C":"C",
                    " ":1453,
                    ".":70,
                    ",":71,
                    "!":72,
                    "?":73,
                    ":":74,
                    ";":75,
                    "'":76,
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
            Incele.harfler.append(csb[Incele.basla+i:Incele.bitir+i]) #harfi al
            Incele.harfler = Incele.harfler + Incele.durak() #durak ekle



        return Incele.harfler


class Sifre():
    sifre_liste = list()

    asal_liste = [11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

    sayı_liste = [10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39,
                  40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72,
                  74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99]

    def sayisal():
        for i in Incele.parcala():
            Sifre.sifre_liste.append(Sezar.latinDeger(i)) # harfleri sayısal değerlerine çevirdik.
        return Sifre.sifre_liste #sayısal değerli liste döner

    def ikilikimlik(): # asil sayılarla ikili kimlik oluşturuyoruz.
        kimlik_sifre = list()
        j = -1
        for i in Sifre.sayisal():
            kimlik_sifre.append(i)
        try:
            for i in range(1,(len(kimlik_sifre)+1) + len(csb)): #girilen kelimenin harf sayısı kadar iki asal sayı ekleneceğinden harf sayısı * 2fazla döndürüyoruz.
                if((i-2) % 3 == 0 or i-2 == 0): #ikinci beşinci yedinci dokuzuncu ... indexlere asal sayi ekleniyor.
                    kimlik_sifre.insert(i,Sifre.asal_liste[random.randint(0,20)])
        except:
            print("Hata!")
        return kimlik_sifre

    def output():
        dosya = open('hash.txt', 'w')

        cikti1 = ''.join(map(str, Sifre.ikilikimlik()))
        cikti2 = ''.join(reversed(cikti1))
        cikti3 = random.uniform(10.000, 50.000)
        cikti4 = random.uniform(50.000, 90.000)

        if(ModAyar.modCek() == "oe"):
            dosya.write(str(cikti4) + cikti1 + cikti2 + str(cikti3))
            return str(cikti4) + cikti1 + cikti2 + str(cikti3)

        elif(ModAyar.modCek() == "oa"):
            dosya.write(cikti1 + str(cikti4) + str(cikti3) + cikti2)
            return cikti1 + str(cikti4) + str(cikti3) + cikti2










def main():
    if(len(csb) % 2 == 0): #kelime uzunluguna gore mod verisi gonderir
        ModAyar.modDegis("oe")
    else:
        ModAyar.modDegis("oa")

    print(Sifre.output())




if __name__ == '__main__':
    main()
