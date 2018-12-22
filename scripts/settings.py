import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import json
from settings_gui import Ui_Form


class SettingsWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main, self.buttons = True, True
        with open('sources/settings.txt', 'r') as f:
            r = json.loads(f.read())
            if r['main_sound'] == 'False':
                self.main = False
            if r['sound_on_click'] == 'False':
                self.buttons = False
        self.buttonBox.accepted.connect(self.save)
        self.buttonBox_2.accepted.connect(lambda: self.set_main(True))
        self.buttonBox_2.rejected.connect(lambda: self.set_main(False))
        self.buttonBox_3.accepted.connect(lambda: self.set_buttons(True))
        self.buttonBox_3.rejected.connect(lambda: self.set_buttons(False))

    def set_main(self, value):
        self.main = value

    def set_buttons(self, value):
        self.buttons = value

    def save(self):
        with open('sources/settings.txt', 'w') as f:
            f.write('{\n    \"main_sound\": \"' + str(self.main) + '\",\n    \"sound_on_click\": \"'
                    + str(self.buttons) + '\"\n}')
            sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SettingsWindow()
    ex.show()
    sys.exit(app.exec())
