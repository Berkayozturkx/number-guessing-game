#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowTitle("Sayı Tahmin Oyunu")
        self.setGeometry(100,100,340,350)
        self.show()
        
    def init_ui(self):
        self.sayi = 0
        baslik = QLabel("Sayı Tahmin Oyunu",self)
        baslik.setGeometry(20, 10, 300, 60)
        
        #font
        font = QFont('Times',14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        
        #Başlığın fontunu ayarlama
        baslik.setFont(font)
        baslik.setAlignment(Qt.AlignCenter)
        
        #Başlığın rengini ayarlama
        renk = QGraphicsColorizeEffect(self)
        renk.setColor(Qt.darkGreen)
        baslik.setGraphicsEffect(renk)
        
        #Bilgi etkiketi ile ilgili işlemler
        self.bilgi = QLabel("Hoşgeldiniz",self)
        self.bilgi.setGeometry(40, 85, 260, 60)
        self.bilgi.setWordWrap(True)
        self.bilgi.setFont(QFont('Times', 13))
        self.bilgi.setAlignment(Qt.AlignCenter)
        self.bilgi.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid black"
                                "background : lightgrey"
                                "}")
        #Spinbox işlemleri
        self.spin = QSpinBox(self)
        self.spin.setRange(1,50)
        self.spin.setGeometry(120, 170, 100, 60)
        self.spin.setAlignment(Qt.AlignCenter)
        self.spin.setFont(QFont('Times',15))
        
        #Kontrol butonu ile ilgili işlemler
        kontrol = QPushButton("Kontrol",self)
        kontrol.setGeometry(130, 235, 80, 30)
        kontrol.clicked.connect(self.kontrol_et)
        
        #Başla butonu ile ilgili işlemler
        basla = QPushButton("Başla",self)
        basla.setGeometry(65, 280, 100, 40)
        basla.clicked.connect(self.baslat)
        mavi = QGraphicsColorizeEffect()
        mavi.setColor(Qt.darkBlue)
        basla.setGraphicsEffect(mavi)
        
        #Sıfırla butonu ile ilgili işlemler
        reset = QPushButton("Sıfırla",self)
        reset.setGeometry(175, 280, 100, 40)
        reset.clicked.connect(self.sifirla)
        kirmizi = QGraphicsColorizeEffect()
        kirmizi.setColor(Qt.red)
        reset.setGraphicsEffect(kirmizi)
                
    def baslat(self):
        self.bilgi.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid black"
                                "background : lightgrey"
                                "}")
        
        self.sayi = random.randint(1, 20)
        self.bilgi.setText("1 ile 20 arasındaki sayıyı tahmin etmeye çalışın")
        
    def kontrol_et(self):
        
        kullaniciSayisi = self.spin.value()
        
        if kullaniciSayisi == self.sayi:
 
            # setting text to the info label
            self.bilgi.setText("Doğru Tahmin")
            # making label green
            self.bilgi.setStyleSheet("QLabel"
                                    "{"
                                    "border : 2px solid black;"
                                    "background : lightgreen;"
                                    "}")
 
        elif kullaniciSayisi < self.sayi:
            self.bilgi.setText("Sayınız daha küçük")
 
        else:
            self.bilgi.setText("Sayınız daha büyük")
            
    def sifirla(self):
        
        self.bilgi.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid black"
                                "background : lightgrey"
                                "}")
        
        self.bilgi.setText("Hoşgeldiniz")
        
        
uygulama = QApplication(sys.argv)
window = Window()
sys.exit(uygulama.exec())


# In[ ]:




