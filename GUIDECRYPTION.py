# © CARULLAH SAİD BERK
from PyQt5 import QtCore, QtGui, QtWidgets
import time

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

    def oaSade(hash): #oa modunu sadeleştirir.
        dosyaoa = open("parcasade.txt","w")
        j = 0
        nt = 0 # ilk nokta tespit edici
        for i in hash: # noktayı bulana dek ara
            if(i == "." and nt == 0): #ilk noktayı bulursan
                parcason = hash[:j-2] #ilk indexten itibaren nokta indeksine kadar hepsini parcason isimli degiskene ata(son iki indeksi alma)
                break # döngüyü durdur

            j = j + 1

        dosyaoa.write(parcason)
        dosyaoa.close()
        Kir.decode()


    def decode(): #gelen sade hash'in sayisal verilerini ayıklar.
        dosyaYaz = open('decrypt.txt', 'w')
        dosyaOku = open('parcasade.txt', 'r')
        parcasade = dosyaOku.read()

        j = 0  # döngü index degiskeni
        tc = 0  # ilk durak tespit degiskeni

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
    osman_tablo = {"21": "a", #boslugu karakter olarak goruyor.
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
                   "97": "j",
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
                   "14": " ",
                   "70":".",
                   "71":",",
                   "72":"!",
                   "73":"?",
                   "74":":",
                   "75":";",
                   "76":"'",
                   "50":"0",
                   "51":"1",
                   "52":"2",
                   "53":"3",
                   "54":"4",
                   "55":"5",
                   "56":"6",
                   "57":"7",
                   "58":"8",
                   "59":"9",
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
     
        dosyaYaz = open("duz_metin.txt", 'w')
        dosyaYaz.write(temiz_metin)

class Ui_OttoCrypto(object):
    def setupUi(self, OttoCrypto):
        OttoCrypto.setObjectName("OttoCrypto")
        OttoCrypto.resize(640, 388)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OttoCrypto.sizePolicy().hasHeightForWidth())
        OttoCrypto.setSizePolicy(sizePolicy)
        OttoCrypto.setMinimumSize(QtCore.QSize(640, 388))
        OttoCrypto.setMaximumSize(QtCore.QSize(640, 388))
        OttoCrypto.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(OttoCrypto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 388))
        self.centralwidget.setMaximumSize(QtCore.QSize(640, 388))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lutfen = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lutfen.setFont(font)
        self.lutfen.setObjectName("lutfen")
        self.verticalLayout.addWidget(self.lutfen)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input.setObjectName("input")
        self.verticalLayout.addWidget(self.input)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.hash = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hash.setObjectName("hash")
        self.verticalLayout.addWidget(self.hash)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        OttoCrypto.setCentralWidget(self.centralwidget)

        self.retranslateUi(OttoCrypto)
        QtCore.QMetaObject.connectSlotsByName(OttoCrypto)

    def retranslateUi(self, OttoCrypto):
        _translate = QtCore.QCoreApplication.translate
        OttoCrypto.setWindowTitle(_translate("OttoCrypto", "OttoCrypto Şifre Çözücü "))
        self.lutfen.setText(_translate("OttoCrypto", "LÜTFEN ÇÖZMEK İSTEDİĞİNİZ ŞİFREYİ GİRİNİZ"))
        self.pushButton.setText(_translate("OttoCrypto", "ÇÖZMEK İÇİN TIKLAYINIZ!"))
        self.hash.setText(_translate("OttoCrypto", "Metninizi duz_metin.txt\'de Bulabilirsiniz."))
        self.pushButton.clicked.connect(self.main)


    def main(self):
        global csb
        csb = self.input.text().strip()
        if(time.strftime("%H"+"%M") == "0415"): #saat 4.15 ise kırılım işlemini başlat
        if(True):
            if(Kir.modCek(csb) == "oe"): # mod oe ise
                Kir.oeSade(csb) #oe sadeleştirmeyi başlat

            elif(Kir.modCek(csb) == "oa"):#mod oa ise
                Kir.oaSade(csb)#oa sadeleştirmeyi başlat.

            dosyaOku = open('duz_metin.txt', 'r').read()
            self.textBrowser.setText(dosyaOku)
        else:
            self.textBrowser.setText("56.38179557644142Q2C4721C9728T7937C4324T97Q7T4737T671453T73Q6T2338T23Q8C4721T5927T1126C4338C6112T6776T2116C8334C6211T7295T1274C8Q32T8332T6Q37T354176T7374T7Q79T4234C7397T8279C1274C2Q29.003378456544905")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OttoCrypto = QtWidgets.QMainWindow()
    ui = Ui_OttoCrypto()
    ui.setupUi(OttoCrypto)
    OttoCrypto.show()
    sys.exit(app.exec_())
