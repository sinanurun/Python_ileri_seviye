from PyQt5.QtWidgets import *
import sys

class ana_pen(QMainWindow):
    def __init__(self):
        super().__init__()
 - 

ana_uyulamasi = QApplication(sys.argv)
ana_penceresi = ana_pen()
ana_penceresi.show()
ana_uyulamasi.exec()