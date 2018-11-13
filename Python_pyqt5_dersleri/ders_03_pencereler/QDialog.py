from PyQt5.QtWidgets import *
import sys

class dialogpen(QDialog):
    def __init__(self):
        super().__init__()


dialog_uyulamasi = QApplication(sys.argv)
dialog_penceresi = dialogpen()
dialog_penceresi.show()
dialog_uyulamasi.exec()