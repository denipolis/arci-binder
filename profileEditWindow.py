# Form implementation generated from reading ui file 'ui/profileEditWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProfileEditWindow(object):
    def setupUi(self, ProfileEditWindow):
        ProfileEditWindow.setObjectName("ProfileEditWindow")
        ProfileEditWindow.resize(941, 411)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ProfileEditWindow.setWindowIcon(icon)
        ProfileEditWindow.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    font-family: Rubik;\n"
"    background-color: #181818\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid #cfcfcf;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"     border-collapse: separate;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #999;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QListWidget {\n"
"    border: 2px solid #cfcfcf;\n"
"    border-radius: 7px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(ProfileEditWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 210, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 60, 851, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.group1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.group1.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.group1.setContentsMargins(0, 0, 0, 0)
        self.group1.setObjectName("group1")
        self.string1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string1.setFont(font)
        self.string1.setText("")
        self.string1.setObjectName("string1")
        self.group1.addWidget(self.string1)
        self.cooldown1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown1.setFont(font)
        self.cooldown1.setObjectName("cooldown1")
        self.group1.addWidget(self.cooldown1)
        self.group1.setStretch(0, 4)
        self.group1.setStretch(1, 1)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(50, 210, 851, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.horizontalLayoutWidget_6.setFont(font)
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.group6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.group6.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.group6.setContentsMargins(0, 0, 0, 0)
        self.group6.setObjectName("group6")
        self.string6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string6.setFont(font)
        self.string6.setObjectName("string6")
        self.group6.addWidget(self.string6)
        self.cooldown6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown6.setFont(font)
        self.cooldown6.setObjectName("cooldown6")
        self.group6.addWidget(self.cooldown6)
        self.group6.setStretch(0, 4)
        self.group6.setStretch(1, 1)
        self.createProfileButton = QtWidgets.QPushButton(self.centralwidget)
        self.createProfileButton.setGeometry(QtCore.QRect(770, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.createProfileButton.setFont(font)
        self.createProfileButton.setStyleSheet("border-radius: 6px;")
        self.createProfileButton.setObjectName("createProfileButton")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(50, 150, 851, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.horizontalLayoutWidget_4.setFont(font)
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.group4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.group4.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.group4.setContentsMargins(0, 0, 0, 0)
        self.group4.setObjectName("group4")
        self.string4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string4.setFont(font)
        self.string4.setObjectName("string4")
        self.group4.addWidget(self.string4)
        self.cooldown4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown4.setFont(font)
        self.cooldown4.setObjectName("cooldown4")
        self.group4.addWidget(self.cooldown4)
        self.group4.setStretch(0, 4)
        self.group4.setStretch(1, 1)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(50, 270, 851, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.horizontalLayoutWidget_8.setFont(font)
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.group8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.group8.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.group8.setContentsMargins(0, 0, 0, 0)
        self.group8.setObjectName("group8")
        self.string8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string8.setFont(font)
        self.string8.setObjectName("string8")
        self.group8.addWidget(self.string8)
        self.cooldown8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown8.setFont(font)
        self.cooldown8.setObjectName("cooldown8")
        self.group8.addWidget(self.cooldown8)
        self.group8.setStretch(0, 4)
        self.group8.setStretch(1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 150, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 40, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(50, 300, 851, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.horizontalLayoutWidget_9.setFont(font)
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.group9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.group9.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.group9.setContentsMargins(0, 0, 0, 0)
        self.group9.setObjectName("group9")
        self.string9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string9.setFont(font)
        self.string9.setObjectName("string9")
        self.group9.addWidget(self.string9)
        self.cooldown9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown9.setFont(font)
        self.cooldown9.setObjectName("cooldown9")
        self.group9.addWidget(self.cooldown9)
        self.group9.setStretch(0, 4)
        self.group9.setStretch(1, 1)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(50, 240, 851, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.horizontalLayoutWidget_7.setFont(font)
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.group7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.group7.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.group7.setContentsMargins(0, 0, 0, 0)
        self.group7.setObjectName("group7")
        self.string7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string7.setFont(font)
        self.string7.setObjectName("string7")
        self.group7.addWidget(self.string7)
        self.cooldown7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown7.setFont(font)
        self.cooldown7.setObjectName("cooldown7")
        self.group7.addWidget(self.cooldown7)
        self.group7.setStretch(0, 4)
        self.group7.setStretch(1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 240, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 300, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 40, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 270, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 180, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(50, 180, 851, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.horizontalLayoutWidget_5.setFont(font)
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.group5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.group5.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.group5.setContentsMargins(0, 0, 0, 0)
        self.group5.setObjectName("group5")
        self.string5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string5.setFont(font)
        self.string5.setObjectName("string5")
        self.group5.addWidget(self.string5)
        self.cooldown5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown5.setFont(font)
        self.cooldown5.setObjectName("cooldown5")
        self.group5.addWidget(self.cooldown5)
        self.group5.setStretch(0, 4)
        self.group5.setStretch(1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 90, 851, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.group2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.group2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.group2.setContentsMargins(0, 0, 0, 0)
        self.group2.setObjectName("group2")
        self.string2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string2.setFont(font)
        self.string2.setObjectName("string2")
        self.group2.addWidget(self.string2)
        self.cooldown2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown2.setFont(font)
        self.cooldown2.setObjectName("cooldown2")
        self.group2.addWidget(self.cooldown2)
        self.group2.setStretch(0, 4)
        self.group2.setStretch(1, 1)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 120, 851, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.horizontalLayoutWidget_3.setFont(font)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.group3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.group3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.group3.setContentsMargins(0, 0, 0, 0)
        self.group3.setObjectName("group3")
        self.string3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string3.setFont(font)
        self.string3.setObjectName("string3")
        self.group3.addWidget(self.string3)
        self.cooldown3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown3.setFont(font)
        self.cooldown3.setObjectName("cooldown3")
        self.group3.addWidget(self.cooldown3)
        self.group3.setStretch(0, 4)
        self.group3.setStretch(1, 1)
        self.shortcutlabel = QtWidgets.QLabel(self.centralwidget)
        self.shortcutlabel.setGeometry(QtCore.QRect(70, 350, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(14)
        self.shortcutlabel.setFont(font)
        self.shortcutlabel.setObjectName("shortcutlabel")
        self.shortcut = QtWidgets.QKeySequenceEdit(self.centralwidget)
        self.shortcut.setGeometry(QtCore.QRect(110, 370, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        self.shortcut.setFont(font)
        self.shortcut.setToolTip("")
        self.shortcut.setObjectName("shortcut")
        self.profileName = QtWidgets.QLineEdit(self.centralwidget)
        self.profileName.setGeometry(QtCore.QRect(430, 370, 181, 21))
        self.profileName.setText("")
        self.profileName.setObjectName("profileName")
        self.profiileNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.profiileNameLabel.setGeometry(QtCore.QRect(470, 350, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(14)
        self.profiileNameLabel.setFont(font)
        self.profiileNameLabel.setObjectName("profiileNameLabel")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(900, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("color: #ffdbdc;")
        self.closeButton.setObjectName("closeButton")
        self.minimizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.minimizeButton.setGeometry(QtCore.QRect(870, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.minimizeButton.setFont(font)
        self.minimizeButton.setStyleSheet("color: #fffde0;")
        self.minimizeButton.setObjectName("minimizeButton")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.title.setStyleSheet("QLabel {\n"
"    color: #fefefe;\n"
"}")
        self.title.setObjectName("title")
        ProfileEditWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ProfileEditWindow)
        self.statusbar.setObjectName("statusbar")
        ProfileEditWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(ProfileEditWindow)
        self.action.setObjectName("action")
        self.action2 = QtGui.QAction(ProfileEditWindow)
        self.action2.setObjectName("action2")

        self.retranslateUi(ProfileEditWindow)
        QtCore.QMetaObject.connectSlotsByName(ProfileEditWindow)

    def retranslateUi(self, ProfileEditWindow):
        _translate = QtCore.QCoreApplication.translate
        ProfileEditWindow.setWindowTitle(_translate("ProfileEditWindow", "Редактирование профиля"))
        self.label_8.setText(_translate("ProfileEditWindow", "6."))
        self.cooldown1.setText(_translate("ProfileEditWindow", "0"))
        self.cooldown6.setText(_translate("ProfileEditWindow", "0"))
        self.createProfileButton.setText(_translate("ProfileEditWindow", "Создать"))
        self.cooldown4.setText(_translate("ProfileEditWindow", "0"))
        self.cooldown8.setText(_translate("ProfileEditWindow", "0"))
        self.label_6.setText(_translate("ProfileEditWindow", "4."))
        self.label_2.setText(_translate("ProfileEditWindow", "Задержка перед написанием"))
        self.label_4.setText(_translate("ProfileEditWindow", "2."))
        self.label_3.setText(_translate("ProfileEditWindow", "1."))
        self.cooldown9.setText(_translate("ProfileEditWindow", "0"))
        self.cooldown7.setText(_translate("ProfileEditWindow", "0"))
        self.label_9.setText(_translate("ProfileEditWindow", "7."))
        self.label_11.setText(_translate("ProfileEditWindow", "9."))
        self.label.setText(_translate("ProfileEditWindow", "Текст"))
        self.label_10.setText(_translate("ProfileEditWindow", "8."))
        self.label_5.setText(_translate("ProfileEditWindow", "3."))
        self.label_7.setText(_translate("ProfileEditWindow", "5."))
        self.cooldown5.setText(_translate("ProfileEditWindow", "0"))
        self.cooldown2.setText(_translate("ProfileEditWindow", "0"))
        self.cooldown3.setText(_translate("ProfileEditWindow", "0"))
        self.shortcutlabel.setText(_translate("ProfileEditWindow", "Горячая клавиша"))
        self.profiileNameLabel.setText(_translate("ProfileEditWindow", " Название"))
        self.closeButton.setText(_translate("ProfileEditWindow", "X"))
        self.minimizeButton.setText(_translate("ProfileEditWindow", "_"))
        self.title.setText(_translate("ProfileEditWindow", "<html><head/><body><p>Редактор профиля</p></body></html>"))
        self.action.setText(_translate("ProfileEditWindow", "Сбросить базу данных"))
        self.action2.setText(_translate("ProfileEditWindow", "Выйти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProfileEditWindow = QtWidgets.QMainWindow()
    ui = Ui_ProfileEditWindow()
    ui.setupUi(ProfileEditWindow)
    ProfileEditWindow.show()
    sys.exit(app.exec())
