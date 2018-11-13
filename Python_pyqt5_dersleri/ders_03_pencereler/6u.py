import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.do_something() #sanity check
        self.cw = ChildWidget(self)
        self.setCentralWidget(self.cw)
        self.show()

    def do_something(self):

        print('doing something!')


class ChildWidget(QWidget):

    def __init__(self, parent):
        super(ChildWidget, self).__init__(parent)

        self.button1 = QPushButton()
        self.button1.clicked.connect(self.do_something_else)

        self.button2 =QPushButton()
        self.button2.clicked.connect(self.parent().do_something)

        self.layout =QVBoxLayout()
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)
        self.show()

    def do_something_else(self):

        print('doing something else!')


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()