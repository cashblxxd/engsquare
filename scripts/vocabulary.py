import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QScrollArea, QHBoxLayout, QInputDialog
import PyQt5.QtGui as QtGui
import csv
import os


class VocabularyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('sources/vocabulary.png'))
        self.word_buttons = {}
        self.d = {}
        self.scores = {}
        self.init_dictionary()
        self.lay = QHBoxLayout()
        self.sA = QScrollArea()
        self.sA_lay = QVBoxLayout()
        self.sA.setLayout(self.sA_lay)
        self.closeGui = QPushButton("Save")
        self.add_file_button = QPushButton("Add Word")
        self.lay.addWidget(self.closeGui)
        self.lay.addWidget(self.add_file_button)
        self.lay.addWidget(self.sA)
        self.setLayout(self.lay)
        self.init_words()
        self.connect_()
        self.show()

    def init_dictionary(self):
        with open('sources/vocabulary.csv', encoding="utf8") as f:
            reader = csv.reader(f, delimiter=';')
            for i in reader:
                self.d[i[0]] = i[1]
                self.scores[i[0]] = float(i[2])

    def init_words(self):
        for i in self.d:
            self.__add_file_to_list(i, self.d[i], self.scores[i])

    def __add_file_to_list(self, i, j, s):
        try:
            self.d[i] = j
            self.scores[i] = s
            k = QPushButton(i)
            k.clicked.connect(self.word_button_click)
            self.sA_lay.addWidget(k)
            self.word_buttons[i] = k
        except Exception: pass

    def word_button_click(self):
        i = self.sender().text()
        j, s = self.d[i], self.scores[i]
        with open("sources/word.txt", 'w') as f:
            f.write(i + '\n' + j + '\n' + str(s))
        os.system("python3 scripts/word_card.py")
        with open('sources/marked.txt', 'r', encoding="utf8") as f:
            for line in f.readlines():
                line = line.strip()
                self.d.pop(line)
                self.scores.pop(line)
                self.word_buttons.pop(i).deleteLater()
        with open('sources/marked.txt', 'w', encoding="utf8") as f:
            f.write('')

    def connect_(self):
        self.add_file_button.clicked.connect(self.add_button_click)
        self.closeGui.clicked.connect(self.close_event)
        return

    def close_event(self):
        with open('sources/vocabulary.csv', 'w', encoding="utf8") as f:
            writer = csv.writer(f, delimiter=';')
            for i in self.d:
                writer.writerow([i, self.d[i], self.scores[i]])
        self.close()

    def add_button_click(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Enter word", "The new word is: "
        )
        if okBtnPressed:
            i = i.split()[0]
            j, okBtnPressed = QInputDialog.getText(
                self, "Enter translation", "The well-known word is: "
            )
            if okBtnPressed:
                j = j.split()[0]
                s, okBtnPressed = QInputDialog.getItem(
                    self,
                    "Enter your level of knowledge of this word",
                    "Select level",
                    ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                     "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26",
                     "27", "28", "29", "30"),
                    1,
                    False
                )
                if okBtnPressed:
                    self.__add_file_to_list(i, j, s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VocabularyWindow()
    ex.show()
    sys.exit(app.exec())
