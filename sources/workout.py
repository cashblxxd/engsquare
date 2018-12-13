import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
import PyQt5.QtGui as QtGui
from PyQt5 import uic
from random import randint
import csv


class WorkoutWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('sources/workout.ui', self)
        self.d = {}
        self.scores = {}
        self.correct = 0
        self.progressBar.setValue(0)
        self.init_dictionary()
        self.words = list(self.d.values())
        while len(self.words) < 5:
            self.words.append('-')
        self.x = list(self.d.keys())
        if not self.x:
            print('Enter at least one word')
            sys.exit()
        self.label.setText(self.x.pop())
        self.answer = self.d[self.label.text()]
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.run)
        self.pushButton_4.clicked.connect(self.run)
        self.pushButton_5.clicked.connect(self.run)
        self.buttons = [
            self.pushButton,
            self.pushButton_2,
            self.pushButton_3,
            self.pushButton_4,
            self.pushButton_5
        ]
        c = self.words.copy()
        c.pop(c.index(self.answer))
        buttons = self.buttons[:]
        buttons.pop(randint(0, 4)).setText(self.answer)
        while buttons:
            s = c.pop(randint(0, len(c) - 1))
            buttons.pop().setText(s)

    def init_dictionary(self):
        with open('sources/vocabulary.csv', encoding="utf8") as f:
            reader = csv.reader(f, delimiter=';')
            for i in reader:
                self.d[i[0]] = i[1]
                self.scores[i[0]] = float(i[2])

    def run(self):
        self.progressBar.setValue(int(100 - (len(self.x) / len(self.d)) * 100))
        if self.label.text() in self.scores:
            if self.sender().text() == self.answer:
                self.correct += 1
                self.scores[self.label.text()] += 1
                self.label_3.setText("Correct\n\nCorrect answer:\n\n" + self.answer)
            else:
                self.scores[self.label.text()] -= 0.8
                self.label_3.setText("Incorrect\n\nCorrect answer:\n\n" + self.answer)
        if not self.x:
            self.end()
            return
        self.label.setText(self.x.pop())
        self.answer = self.d[self.label.text()]
        c = self.words.copy()
        c.pop(c.index(self.answer))
        buttons = self.buttons[:]
        buttons.pop(randint(0, 4)).setText(self.answer)
        while buttons:
            buttons.pop().setText(c.pop(randint(0, len(c) - 1)))

    def end(self):
        for i in self.buttons:
            i.setText('-')
        self.label.setText("{0:.2f}".format(self.correct / len(self.d) * 100) + ' %')
        with open('sources/vocabulary.csv', 'w', encoding="utf8") as f:
            writer = csv.writer(f, delimiter=';')
            for i in self.d:
                writer.writerow([i, self.d[i], self.scores[i]])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WorkoutWindow()
    ex.show()
    sys.exit(app.exec())
