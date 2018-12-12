import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
import PyQt5.QtGui as QtGui
from PyQt5 import uic
import json


class WorkoutWindow(QMainWindow, QWidget):
    def __init__(self):#, vocabulary, count):
        super().__init__()
        uic.loadUi('workout.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):#, vocabulary, count):
        print('Hello')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WorkoutWindow()
    ex.show()
    sys.exit(app.exec())