csb = input("Lütfen Şifrelemek İstediğiniz Metni Giriniz: ")


class ModAyar():

    def modDegis(encryptionMod): # sifreleme modunu kelime uzunluguna gore belirler
        dosya = open('mod.txt', 'w')
        dosya.write(encryptionMod)

    def modCek(): # sifreleme modunu her cagrildiginda geri dondurur.
        dosya = open('mod.txt', 'r')
        for satir in dosya:
            return satir

class Sezar:
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






def main():
    if(len(csb) % 2 == 0): #kelime uzunluguna gore mod verisi gonderir
        ModAyar.modDegis("oe")
    else:
        ModAyar.modDegis("oa")

    print(Sezar.latinDeger("a")) # latince sayısal karşılığı verir




if __name__ == '__main__':
    main()
