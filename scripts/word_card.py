import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QProgressBar
from PyQt5 import QtGui, QtCore
import os
import json


class WordCard(QWidget):
    def __init__(self, i, j, s):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('sources/word_icon.png'))
        s = int(float(s))
        self.i = i
        self.setGeometry(700, 500, 720, 150)
        self.setWindowTitle(i)

        self.coords = QLabel(self)
        self.coords.setText("Word: " + i)
        self.coords.move(30, 30)

        self.coords1 = QLabel(self)
        self.coords1.setText("Translation: " + j)
        self.coords1.move(30, 60)

        self.progressBar = QProgressBar(self)
        self.progressBar.setValue(int((s / 30) * 100))
        self.progressBar.move(30, 90)
        self.progressBar.resize(150, 20)

        self.deleter = QPushButton(self)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("sources/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleter.setIcon(icon2)
        self.deleter.setIconSize(QtCore.QSize(86, 86))
        self.deleter.resize(100, 100)
        self.deleter.move(500, 20)
        self.deleter.clicked.connect(self.delete_button)

        self.speaker = QPushButton(self)
        icon = QtGui.QIcon()
        with open('sources/settings.txt', 'r') as f:
            r = json.loads(f.read())
            if r['main_sound'] == 'True':
                icon.addPixmap(QtGui.QPixmap("sources/sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            if r['main_sound'] == 'False':
                icon.addPixmap(QtGui.QPixmap("sources/sound_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speaker.setIcon(icon)
        self.speaker.setIconSize(QtCore.QSize(86, 86))
        self.speaker.resize(100, 100)
        self.speaker.move(610, 20)
        self.speaker.clicked.connect(self.speak)

    def delete_button(self):
        with open('sources/marked.txt', 'w+', encoding="utf8") as f:
            f.write(self.i + '\n')
        sys.exit()

    def speak(self):
        with open('sources/word_to_tell.txt', 'w') as f:
            f.write(self.coords.text())
        os.system("python3 scripts/speaker.py")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("sources/word.txt", 'r') as f:
        i, j, s = map(str.strip, f.readlines())
    ex = WordCard(i, j, s)
    ex.show()
    sys.exit(app.exec_())
