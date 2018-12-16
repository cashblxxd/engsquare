import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import PyQt5.QtGui as QtGui
from random import randint
import csv
from scripts.game_gui import Ui_Workout_session


class GameWindow(QMainWindow,Ui_Workout_session):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.d = {}
        self.scores = {}
        self.correct = 0
        self.init_dictionary()
        self.length = len(self.d)
        self.words = list(self.d.values())
        self.x = list(self.d.keys())
        self.label.setText(self.x.pop(randint(0, self.length)))
        self.label_3.setText('-')
        self.answer = self.d[self.label.text()]
        self.pushButton_5.clicked.connect(self.run)
        self.pushButton_7.clicked.connect(self.run)
        self.pushButton_8.clicked.connect(self.run)
        self.pushButton_9.clicked.connect(self.run)
        self.pushButton_10.clicked.connect(self.run)
        self.pushButton_12.clicked.connect(self.run)
        self.pushButton_13.clicked.connect(self.run)
        self.pushButton_11.clicked.connect(self.add_to_dictionary)
        self.buttons = [
            self.pushButton_5,
            self.pushButton_7,
            self.pushButton_8,
            self.pushButton_9,
            self.pushButton_10,
            self.pushButton_12,
            self.pushButton_13
        ]
        self.icon2 = QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap("sources/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        c = self.words.copy()
        c.pop(c.index(self.answer))
        buttons = self.buttons[:]
        buttons.pop(randint(0, 4)).setText(self.answer)
        while buttons:
            s = c.pop(randint(0, len(c) - 1))
            buttons.pop().setText(s)

    def add_to_dictionary(self):
        with open('sources/vocabulary.csv', 'a+', encoding="utf8") as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([self.label.text(), self.answer, self.scores[self.label.text()]])
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sources/check.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sender().setIcon(icon)

    def init_dictionary(self):
        with open('sources/game.csv', encoding="utf8") as f:
            reader = csv.reader(f, delimiter=';')
            for i in reader:
                self.d[i[0]] = i[1]
                self.scores[i[0]] = float(i[2])

    def run(self):
        if self.label.text() in self.scores:
            if self.sender().text() == self.answer:
                self.correct += 1
                self.scores[self.label.text()] += 1
                self.label_3.setText("CORRECT!")
            else:
                self.scores[self.label.text()] -= 0.8
                self.label_3.setText("INCORRECT!\n\nCorrect:\n\n" + '\n'.join(self.answer.split()))
        self.pushButton_11.setIcon(self.icon2)
        self.label.setText(self.x.pop(randint(0, self.length)))
        self.answer = self.d[self.label.text()]
        c = self.words.copy()
        c.pop(c.index(self.answer))
        buttons = self.buttons[:]
        buttons.pop(randint(0, 4)).setText(self.answer)
        while buttons:
            buttons.pop().setText(c.pop(randint(0, len(c) - 1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GameWindow()
    ex.show()
    sys.exit(app.exec())
