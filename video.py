from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import QTimer

from GUI import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.mediaPlayer = QtMultimedia.QMediaPlayer(self)
        self.mediaPlayer.setVideoOutput(self.widget)
        # fileName = "/path/of/your/local_file"
        # url = QtCore.QUrl.fromLocalFile(fileName)
        url = QtCore.QUrl("http://clips.vorwaerts-gmbh.de/VfE_html5.mp4")
        self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(url))
        self.mediaPlayer.play()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()