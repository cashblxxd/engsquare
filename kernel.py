import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
from engsquare import Ui_StartWIndow


class StartWindow(QMainWindow, Ui_StartWIndow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.vocabulary, self.count = {}, 0
        self.pushButton.clicked.connect(self.run_workout)
        self.pushButton_2.clicked.connect(self.run_vocabulary)
        self.pushButton_3.clicked.connect(self.run_game)
        self.pushButton_4.clicked.connect(self.run_settings)

    def run_workout(self):
        os.system("python3 scripts/workout.py")

    def run_vocabulary(self):
        os.system("python3 scripts/vocabulary.py")
        self.update_progress()

    def run_game(self):
        os.system("python3 scripts/game.py")

    def run_settings(self):
        os.system("python3 scripts/settings.py")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    sys.exit(app.exec())
