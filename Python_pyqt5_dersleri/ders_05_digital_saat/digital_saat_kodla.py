from PyQt5.QtWidgets import *
from PyQt5.QtCore import * #QTimer, QTime
from PyQt5.QtGui import * #QColor, QIcon
import sys

class Clock(QLCDNumber):
    def __init__(self):
        super().__init__()

        baslik = "Digital Saat"
        ust = 350
        sol = 350
        genislik = 400
        yukseklik = 400

        renkler = self.palette()

        #text renkgini belirlemek için
        renkler.setColor(renkler.WindowText, QColor("red")) # "renk" yerine kod da kullanılabilir 204,204,0 gibi

        # pencerenin rengini belirlemek için
        renkler.setColor(renkler.Window,QColor("yellow"))
        # belirlenen renkerli uygulamak için
        self.setPalette(renkler)

        self.setWindowTitle(baslik)
        self.setGeometry(ust,sol,genislik,yukseklik)


        self.setSegmentStyle(QLCDNumber.Filled)
        zamanlayici = QTimer(self)
        zamanlayici.timeout.connect(self.zamanigoster)
        zamanlayici.start(1000)
        self.zamanigoster()


    def zamanigoster(self):
        zaman = QTime.currentTime()
        metin = zaman.toString('hh:mm')
        print(metin)
        if (zaman.second()%2) == 0:
            metin = metin[:2]+ " " + metin[3:]

        self.display(metin)

uygulama = QApplication(sys.argv)
saat = Clock()
saat.show()
uygulama.exec()