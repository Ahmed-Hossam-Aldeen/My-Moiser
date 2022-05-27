from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QFileDialog
import sys
from PyQt5.uic.properties import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import Qt, QUrl
from functools import partial

def hhmmss(ms):
    # s = 1000
    # m = 60000
    # h = 360000
    h, r = divmod(ms, 36000)
    m, r = divmod(r, 60000)
    s, _ = divmod(r, 1000)
    return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('Moiser.ui', self)

        self.player1 = QMediaPlayer()
        self.player2 = QMediaPlayer()
        self.player3 = QMediaPlayer()
        self.player4 = QMediaPlayer()

        self.upload1.clicked.connect(partial(self.clicked_btn, 'vocals'))
        self.upload2.clicked.connect(partial(self.clicked_btn, 'melody'))
        self.upload3.clicked.connect(partial(self.clicked_btn, 'drums'))
        self.upload4.clicked.connect(partial(self.clicked_btn, 'bass'))


        self.player1.durationChanged.connect(self.update_duration)
        self.player1.positionChanged.connect(self.update_position)
        self.horizontalSlider.valueChanged.connect(self.player1.setPosition)
        self.horizontalSlider.valueChanged.connect(self.player2.setPosition)
        self.horizontalSlider.valueChanged.connect(self.player3.setPosition)
        self.horizontalSlider.valueChanged.connect(self.player4.setPosition)

        self.play.clicked.connect(self.PlaySongs)
        self.stopAll.clicked.connect(self.StopSongs)
        self.volumeVocals.valueChanged.connect(self.player1.setVolume)
        self.volumeOther.valueChanged.connect(self.player2.setVolume)
        self.volumeDrums.valueChanged.connect(self.player3.setVolume)
        self.volumeBass.valueChanged.connect(self.player4.setVolume)

        self.show()

    def clicked_btn(self, value):
        print(f'{value} clicked')
        path = QFileDialog.getOpenFileName(self, 'Open a file', '', 'Audio File(*.mp3)')

        if path != ('', ''):
            data = path[0]

            if value == "vocals":
                self.player1.setMedia(QMediaContent(QUrl.fromLocalFile(data)))
                print("vocals uploaded!")
            elif value == "melody":
                self.player2.setMedia(QMediaContent(QUrl.fromLocalFile(data))) 
                print("melody uploaded!")   
            elif value == "drums":
                self.player3.setMedia(QMediaContent(QUrl.fromLocalFile(data))) 
                print("drums uploaded!")              
            elif value == "bass":
                self.player4.setMedia(QMediaContent(QUrl.fromLocalFile(data)))
                print("bass uploaded!")     

    def PlaySongs(self):
        val = self.horizontalSlider.value()

        self.player1.setPosition(val)
        self.player2.setPosition(val)
        self.player3.setPosition(val)
        self.player4.setPosition(val)

        self.player1.play()
        self.player2.play()
        self.player3.play()
        self.player4.play()

    def StopSongs(self):
        self.player1.stop()
        self.player2.stop()
        self.player3.stop()
        self.player4.stop()

    def update_duration(self, duration):
        self.horizontalSlider.setMaximum(duration)

    def update_position(self, position):
        self.horizontalSlider.blockSignals(True)
        self.horizontalSlider.setValue(position)
        self.horizontalSlider.blockSignals(False)  

app = 0
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()