# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random



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
                    "0":50,
                    "1":51,
                    "2":52,
                    "3":53,
                    "4":54,
                    "5":55,
                    "6":56,
                    "7":57,
                    "8":58,
                    "9":59,
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



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 388)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lutfen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lutfen.setObjectName("lutfen")
        self.verticalLayout.addWidget(self.lutfen)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input.setObjectName("input")
        self.verticalLayout.addWidget(self.input)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.hash = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hash.setObjectName("hash")
        self.verticalLayout.addWidget(self.hash)
        self.hashtxt = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hashtxt.sizePolicy().hasHeightForWidth())
        self.hashtxt.setSizePolicy(sizePolicy)
        self.hashtxt.setText("")
        self.hashtxt.setObjectName("hashtxt")
        self.verticalLayout.addWidget(self.hashtxt)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
	

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lutfen.setText(_translate("MainWindow", "LÜTFEN ŞİFRELEMEK İSTEDİĞİNİZ METNİ GİRİNİZ:"))
        self.pushButton.setText(_translate("MainWindow", "ŞİFRELE!"))
        self.hash.setText(_translate("MainWindow", "Şifrenizi Hash .txt\'de Bulabilirsiniz."))
        self.pushButton.clicked.connect(self.main)
   
    def main(self):
        global csb
        print(self.input.text())
        metin = self.input.text()
        csb = metin.lower()  # inputu alıp küçük harflere döküyoruz.


        if(len(csb) % 2 == 0): #kelime uzunluguna gore mod verisi gonderir
            ModAyar.modDegis("oe")
        else:
            ModAyar.modDegis("oa")
        self.hash.setText(Sifre.output())
       

	


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.main()
    MainWindow.show()
    sys.exit(app.exec_())
