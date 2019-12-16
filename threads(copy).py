import sys

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtCore import QRect, pyqtSlot
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLineEdit, QMessageBox


class VideoWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(VideoWindow, self).__init__(parent)

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

        #Heading of the window .
        self.label = QtWidgets.QLabel(self)
        self.label.setText("<h2>ChargePay Welcomes you</h2>")
        self.label.setGeometry(QRect(150, -30, 525, 145))
        self.label.setStyleSheet('color:darkred')


        # state of charge
        button1 = QPushButton(" SOC ", self)
        button1.setGeometry(QRect(540, 100, 100, 45))
        button1.resize(50, 35)
        button1.setToolTip("STATE OF CHARGE")

        # soc output
        button1 = QPushButton("  ", self)
        button1.setGeometry(QRect(670, 100, 100, 45))
        button1.resize(60, 35)
        button1.setToolTip("STATE OF CHARGE")

        # required units
        button1 = QPushButton(" UNITS ", self)
        button1.setGeometry(QRect(540, 170, 100, 45))
        button1.resize(50, 35)
        button1.setToolTip("Units needed for the user ")

        # input fields for charging
        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(QRect(670, 170, 100, 45))
        self.textbox.resize(60, 35)

        # Create a button in the window
        self.button = QPushButton(" Charge  ", self)
        self.button.setGeometry(QRect(600, 250, 100, 45))
        self.button.setIcon(QtGui.QIcon("icon.png"))
        self.button.setIconSize(QtCore.QSize(30, 30))
        self.button.setToolTip("Proceed to Charge")

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

        #video player code
        self.mediaPlayer = QtMultimedia.QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)

        videoWidget = QtMultimediaWidgets.QVideoWidget()

        container = QtWidgets.QWidget()
        lay = QtWidgets.QVBoxLayout(container)
        lay.setContentsMargins(0, 40, 300, 0)
        lay.addWidget(videoWidget)



        self.playButton = QtWidgets.QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QtWidgets.QLabel()
        self.errorLabel.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                      QtWidgets.QSizePolicy.Maximum)

        # Create new action
        openAction = QtWidgets.QAction(QtGui.QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('CAAS')
        openAction.triggered.connect(self.openFile)

        # Create exit action
        exitAction = QtWidgets.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        # # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        # fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

        # # Create a widget for window contents
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)

        # Create layouts to place inside widget
        controlLayout = QtWidgets.QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(container)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)

        # Set widget to contain window contents
        wid.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

     # Onclick function for units to charge
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        print(textboxValue)

        self.textbox.setText("")

    # video player code
    def openFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Movie",
                                                            QtCore.QDir.homePath())

        if fileName:
            self.mediaPlayer.setMedia(
                QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def play(self):
        if self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    player = VideoWindow()
    player.resize(800, 470)
    player.show()
    sys.exit(app.exec_())
