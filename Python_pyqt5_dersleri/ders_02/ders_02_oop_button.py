import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont

class p_sinifi(QWidget):
    def __init__(self):
        super().__init__()
        self.ekran_tasarla()

    def ekran_tasarla(self):
        QToolTip.setFont(QFont('verdana',22))
        self.setToolTip("bu bir penceredir")
        buton_01 = QPushButton("Düğme_tıklanabilir",self)
        buton_01.clicked.connect(self.tiklandi)
        buton_01.move(100,100)
        buton_01.setToolTip("bu tıklanabilir bir butondur")
        self.setGeometry(150,250,500,300)
        self.setWindowTitle("Buton Uygulaması")
        self.show()
    def tiklandi(self):
        print("butona tıklandı")
if __name__ =='__main__':
    uygulama = QApplication(sys.argv)
    pencere = p_sinifi()
    sys.exit(uygulama.exec())