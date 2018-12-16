from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_Workout_session(object):
    def setupUi(self, Workout_session):
        Workout_session.setObjectName("Workout_session")
        Workout_session.resize(949, 619)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sources/game_icon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Workout_session.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Workout_session)
        self.label.setGeometry(QtCore.QRect(140, 10, 791, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nimbus Roman No9 L")
        font.setPointSize(64)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(Workout_session)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 130, 801, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.icon1 = QtGui.QIcon()
        self.icon1.addPixmap(QtGui.QPixmap("sources/sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(Workout_session)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 101, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_6 = QtWidgets.QPushButton(Workout_session)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 10, 121, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(20)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("sources/sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_11 = QtWidgets.QPushButton(Workout_session)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 460, 111, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(20)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("sources/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setIconSize(QtCore.QSize(86, 86))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_7 = QtWidgets.QPushButton(Workout_session)
        self.pushButton_7.setGeometry(QtCore.QRect(130, 270, 801, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Workout_session)
        self.pushButton_8.setGeometry(QtCore.QRect(130, 200, 801, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Workout_session)
        self.pushButton_9.setGeometry(QtCore.QRect(130, 340, 801, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Workout_session)
        self.pushButton_10.setGeometry(QtCore.QRect(130, 410, 801, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_12 = QtWidgets.QPushButton(Workout_session)
        self.pushButton_12.setGeometry(QtCore.QRect(130, 480, 801, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Workout_session)
        self.pushButton_13.setGeometry(QtCore.QRect(130, 550, 801, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setObjectName("pushButton_13")
        with open('sources/settings.txt', 'r') as f:
            r = json.loads(f.read())
            if r['main_sound'] == 'True':
                self.activate_main_sound()
            if r['main_sound'] == 'False':
                self.deactivate_sound()
            if r['sound_on_click'] == 'True':
                self.activate_sound()

        self.retranslateUi(Workout_session)
        QtCore.QMetaObject.connectSlotsByName(Workout_session)

    def activate_sound(self):
        self.pushButton_5.setIcon(self.icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_7.setIcon(self.icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_8.setIcon(self.icon1)
        self.pushButton_8.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_9.setIcon(self.icon1)
        self.pushButton_9.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_10.setIcon(self.icon1)
        self.pushButton_10.setIconSize(QtCore.QSize(32, 32))

    def activate_main_sound(self):
        self.pushButton_6.setIcon(self.icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(86, 86))

    def deactivate_sound(self):
        self.icon2 = QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap("sources/sound_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(self.icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(86, 86))

    def retranslateUi(self, Workout_session):
        _translate = QtCore.QCoreApplication.translate
        Workout_session.setWindowTitle(_translate("Workout_session", "Dojo"))
        self.label.setText(_translate("Workout_session", "TextLabel"))
        self.pushButton_5.setText(_translate("Workout_session", "   PushButton"))
        self.label_3.setText(_translate("Workout_session", "TextLabel"))
        self.pushButton_7.setText(_translate("Workout_session", "   PushButton"))
        self.pushButton_8.setText(_translate("Workout_session", "   PushButton"))
        self.pushButton_9.setText(_translate("Workout_session", "   PushButton"))
        self.pushButton_10.setText(_translate("Workout_session", "   PushButton"))
        self.pushButton_12.setText(_translate("Workout_session", "   PushButton"))
        self.pushButton_13.setText(_translate("Workout_session", "   PushButton"))
