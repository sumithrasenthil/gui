from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog,QLabel, QVBoxLayout,QHBoxLayout,QGroupBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5 import QtWidgets


class window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "CAAS"
        self.top = 0
        self.left = 100
        self.width = 800
        self.height = 470
        self.Iconimage = "icon.png"

        self.InitWindow()
        self.show()



    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.Iconimage))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.Uicomponent()



    def Uicomponent(self):
        vbox=QVBoxLayout()

        self.label = QtWidgets.QLabel(self)
        self.label.setText("<h2>Welcome to ChargePay</h5>")
        # self.label.move(100,100)
        self.label.setGeometry(QRect(150,0, 525,145))
        # vbox.addWidget(self.label)
        self.label.setFont(QtGui.QFont("Bitter",18))
        self.setStyleSheet('color:darkred')
        button = QPushButton(" Charge  ", self)
        button.setGeometry(QRect(350, 350, 100, 45))
        button.setIcon(QtGui.QIcon("icon.png"))
        button.setIconSize(QtCore.QSize(30, 30))
        button.setToolTip("Proceed to Charge")
        # button.clicked.connect(self.Clickme)






    # def Clickme(self):
    #     sys.exit()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = window()
    sys.exit(App.exec())
