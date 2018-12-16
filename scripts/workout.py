import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
import csv
import os
from dojo import Ui_Workout_session
import json


class WorkoutWindow(QMainWindow,Ui_Workout_session):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.d = {}
        self.scores = {}
        self.correct = 0
        self.session_progress.setValue(0)
        self.init_dictionary()
        self.words = list(self.d.values())
        while len(self.words) < 5:
            self.words.append('-')
        self.x = list(self.d.keys())
        self.buttons = [
            self.pushButton_5,
            self.pushButton_7,
            self.pushButton_8,
            self.pushButton_9,
            self.pushButton_10
        ]
        if not self.x:
            sys.exit()
        for i in self.buttons:
            i.clicked.connect(self.run)
        self.label.setText(self.x.pop(randint(0, len(self.x) - 1)))
        self.label_3.setText('-')
        self.answer = self.d[self.label.text()]
        c = self.words.copy()
        c.pop(c.index(self.answer))
        buttons = self.buttons[:]
        buttons.pop(randint(0, 4)).setText(self.answer)
        while buttons:
            s = c.pop(randint(0, len(c) - 1))
            buttons.pop().setText(s)
        self.button_sound = False
        with open('sources/settings.txt', 'r') as f:
            r = json.loads(f.read())
            if r['main_sound'] == 'True':
                self.pushButton_6.clicked.connect(self.speak)
            if r['sound_on_click'] == 'True':
                self.button_sound = True

    def speak(self):
        with open('sources/word_to_tell.txt', 'w') as f:
            f.write(self.label.text())
        os.system("python3 scripts/speaker.py")

    def button_speak(self, text):
        with open('sources/word_to_tell.txt', 'w') as f:
            f.write(text)
        os.system("python3 scripts/speaker.py")

    def init_dictionary(self):
        with open('sources/vocabulary.csv', encoding="utf8") as f:
            reader = csv.reader(f, delimiter=';')
            for i in reader:
                self.d[i[0]] = i[1]
                self.scores[i[0]] = float(i[2])

    def run(self):
        self.session_progress.setValue(int(100 - (len(self.x) / len(self.d)) * 100))
        if self.label.text() in self.scores:
            if self.sender().text() == self.answer:
                self.correct += 1
                self.scores[self.label.text()] += 1
                self.label_3.setText("CORRECT!")
            else:
                self.scores[self.label.text()] -= 0.8
                self.label_3.setText("INCORRECT!\n\nCorrect:\n\n" + '\n'.join(self.answer.split()))
        if not self.x:
            self.end()
            return
        if self.button_sound:
            self.button_speak(self.sender().text())
        self.label.setText(self.x.pop(randint(0, len(self.x) - 1)))
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
