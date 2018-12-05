from PyQt5.QtWidgets import *
from PyQt5.uic import *
import sys

class pencere(QDialog):
    def __init__(self,parent=None):
        super(pencere,self).__init__(parent)
        loadUi("ornek01.ui",self)
    def deneme(self):
        print("merhaba")
    def accept(self):
        print("kabul edildi")
        self.close()



uyglama = QApplication(sys.argv)
x = pencere()
x.show()
# dialog.buttonBox.accepted.connect(deneme)
# dialog.pushButton.clicked.connect(accepted)
# dialog.buttonBox.accepted()
uyglama.exec()
