from PyQt5.QtWidgets import *
import sys

class widget_pen(QWidget):
    def __init__(self):
        super().__init__()


widget_uyulamasi = QApplication(sys.argv)
widget_penceresi = widget_pen()
widget_penceresi.show()
widget_uyulamasi.exec()