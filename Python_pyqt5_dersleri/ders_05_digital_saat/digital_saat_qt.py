from PyQt5.QtWidgets import *
from PyQt5.QtCore import * #QTimer, QTime
from PyQt5.QtGui import * #QColor, QIcon
from PyQt5.uic import *
import sys


class Clock(QWidget):
    def __init__(self):
        super(Clock,self).__init__()
        self.pencere = loadUi("saatarayuzu.ui",self)


        self.gosterge = self.pencere.lcdNumber
        self.gosterge.setSegmentStyle(QLCDNumber.Filled)
        zamanlayici = QTimer(self)
        zamanlayici.timeout.connect(self.zamanigoster)
        zamanlayici.start(1000)
        self.zamanigoster()


    def zamanigoster(self):
        zaman = QTime.currentTime()
        metin = zaman.toString('hh:mm')
        print(metin)
        if (zaman.second() % 2) == 0:
            metin = metin[:2] + " " + metin[3:]

        self.gosterge.display(metin)


uygulama = QApplication(sys.argv)
saat = Clock()
saat.show()
uygulama.exec()