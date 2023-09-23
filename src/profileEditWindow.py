# Form implementation generated from reading ui file 'src/ui/profileEditWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProfileEditWindow(object):
    def setupUi(self, ProfileEditWindow):
        ProfileEditWindow.setObjectName("ProfileEditWindow")
        ProfileEditWindow.resize(967, 503)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ProfileEditWindow.setWindowIcon(icon)
        ProfileEditWindow.setStyleSheet("QWidget {\n"
"   background-color: #13171c;\n"
"   color: #f5f5f5;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid #cfcfcf;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1d2024;\n"
"    border: none;\n"
"     border-collapse: separate;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #222a33;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: #1d2329;\n"
"}\n"
"\n"
"QListWidget {\n"
"    border: 2px solid #cfcfcf;\n"
"    border-radius: 7px;\n"
"}")
        self.centralWidget = QtWidgets.QWidget(ProfileEditWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.createProfileButton = QtWidgets.QPushButton(self.centralWidget)
        self.createProfileButton.setGeometry(QtCore.QRect(410, 460, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.createProfileButton.setFont(font)
        self.createProfileButton.setStyleSheet("border-radius: 6px;")
        self.createProfileButton.setObjectName("createProfileButton")
        self.shortcutlabel = QtWidgets.QLabel(self.centralWidget)
        self.shortcutlabel.setGeometry(QtCore.QRect(550, 400, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(14)
        self.shortcutlabel.setFont(font)
        self.shortcutlabel.setStyleSheet("QLabel {\n"
"    color: rgb(220, 220, 220)\n"
"}")
        self.shortcutlabel.setObjectName("shortcutlabel")
        self.shortcut = QtWidgets.QKeySequenceEdit(self.centralWidget)
        self.shortcut.setGeometry(QtCore.QRect(550, 430, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        self.shortcut.setFont(font)
        self.shortcut.setToolTip("")
        self.shortcut.setKeySequence("")
        self.shortcut.setObjectName("shortcut")
        self.profileName = QtWidgets.QLineEdit(self.centralWidget)
        self.profileName.setGeometry(QtCore.QRect(340, 430, 181, 21))
        self.profileName.setText("")
        self.profileName.setObjectName("profileName")
        self.profiileNameLabel = QtWidgets.QLabel(self.centralWidget)
        self.profiileNameLabel.setGeometry(QtCore.QRect(340, 400, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(14)
        self.profiileNameLabel.setFont(font)
        self.profiileNameLabel.setStyleSheet("QLabel {\n"
"    color: rgb(220, 220, 220)\n"
"}")
        self.profiileNameLabel.setObjectName("profiileNameLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 921, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.group1 = QtWidgets.QHBoxLayout()
        self.group1.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.group1.setSpacing(10)
        self.group1.setObjectName("group1")
        self.label1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label1.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label1.setObjectName("label1")
        self.group1.addWidget(self.label1)
        self.string1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string1.setFont(font)
        self.string1.setText("")
        self.string1.setObjectName("string1")
        self.group1.addWidget(self.string1)
        self.cooldown1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown1.setFont(font)
        self.cooldown1.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.cooldown1.setObjectName("cooldown1")
        self.group1.addWidget(self.cooldown1)
        self.group1.setStretch(1, 10)
        self.verticalLayout.addLayout(self.group1)
        self.group2 = QtWidgets.QHBoxLayout()
        self.group2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.group2.setSpacing(10)
        self.group2.setObjectName("group2")
        self.label2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label2.setObjectName("label2")
        self.group2.addWidget(self.label2)
        self.string2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string2.setFont(font)
        self.string2.setObjectName("string2")
        self.group2.addWidget(self.string2)
        self.cooldown2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown2.setFont(font)
        self.cooldown2.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.cooldown2.setObjectName("cooldown2")
        self.group2.addWidget(self.cooldown2)
        self.group2.setStretch(1, 10)
        self.verticalLayout.addLayout(self.group2)
        self.group3 = QtWidgets.QHBoxLayout()
        self.group3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.group3.setSpacing(10)
        self.group3.setObjectName("group3")
        self.label3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.label3.setFont(font)
        self.label3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label3.setObjectName("label3")
        self.group3.addWidget(self.label3)
        self.string3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string3.setFont(font)
        self.string3.setObjectName("string3")
        self.group3.addWidget(self.string3)
        self.cooldown3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown3.setFont(font)
        self.cooldown3.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.cooldown3.setObjectName("cooldown3")
        self.group3.addWidget(self.cooldown3)
        self.group3.setStretch(1, 10)
        self.verticalLayout.addLayout(self.group3)
        self.group4 = QtWidgets.QHBoxLayout()
        self.group4.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.group4.setSpacing(10)
        self.group4.setObjectName("group4")
        self.label4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.label4.setFont(font)
        self.label4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label4.setObjectName("label4")
        self.group4.addWidget(self.label4)
        self.string4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string4.setFont(font)
        self.string4.setObjectName("string4")
        self.group4.addWidget(self.string4)
        self.cooldown4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown4.setFont(font)
        self.cooldown4.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.cooldown4.setObjectName("cooldown4")
        self.group4.addWidget(self.cooldown4)
        self.group4.setStretch(1, 10)
        self.verticalLayout.addLayout(self.group4)
        self.group5 = QtWidgets.QHBoxLayout()
        self.group5.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.group5.setSpacing(10)
        self.group5.setObjectName("group5")
        self.label5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.label5.setFont(font)
        self.label5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label5.setObjectName("label5")
        self.group5.addWidget(self.label5)
        self.string5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string5.setFont(font)
        self.string5.setObjectName("string5")
        self.group5.addWidget(self.string5)
        self.cooldown5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown5.setFont(font)
        self.cooldown5.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.cooldown5.setObjectName("cooldown5")
        self.group5.addWidget(self.cooldown5)
        self.group5.setStretch(1, 10)
        self.verticalLayout.addLayout(self.group5)
        self.group6 = QtWidgets.QHBoxLayout()
        self.group6.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.group6.setSpacing(10)
        self.group6.setObjectName("group6")
        self.label6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.label6.setFont(font)
        self.label6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label6.setObjectName("label6")
        self.group6.addWidget(self.label6)
        self.string6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string6.setFont(font)
        self.string6.setObjectName("string6")
        self.group6.addWidget(self.string6)
        self.cooldown6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown6.setFont(font)
        self.cooldown6.setObjectName("cooldown6")
        self.group6.addWidget(self.cooldown6)
        self.group6.setStretch(1, 10)
        self.verticalLayout.addLayout(self.group6)
        self.group7 = QtWidgets.QHBoxLayout()
        self.group7.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.group7.setSpacing(10)
        self.group7.setObjectName("group7")
        self.label7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.label7.setFont(font)
        self.label7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label7.setObjectName("label7")
        self.group7.addWidget(self.label7)
        self.string7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string7.setFont(font)
        self.string7.setObjectName("string7")
        self.group7.addWidget(self.string7)
        self.cooldown7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown7.setFont(font)
        self.cooldown7.setObjectName("cooldown7")
        self.group7.addWidget(self.cooldown7)
        self.group7.setStretch(1, 10)
        self.verticalLayout.addLayout(self.group7)
        self.group8 = QtWidgets.QHBoxLayout()
        self.group8.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.group8.setSpacing(10)
        self.group8.setObjectName("group8")
        self.label8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.label8.setFont(font)
        self.label8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label8.setObjectName("label8")
        self.group8.addWidget(self.label8)
        self.string8 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string8.setFont(font)
        self.string8.setObjectName("string8")
        self.group8.addWidget(self.string8)
        self.cooldown8 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown8.setFont(font)
        self.cooldown8.setObjectName("cooldown8")
        self.group8.addWidget(self.cooldown8)
        self.group8.setStretch(1, 10)
        self.verticalLayout.addLayout(self.group8)
        self.group9 = QtWidgets.QHBoxLayout()
        self.group9.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.group9.setSpacing(10)
        self.group9.setObjectName("group9")
        self.label9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.label9.setFont(font)
        self.label9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label9.setObjectName("label9")
        self.group9.addWidget(self.label9)
        self.string9 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.string9.setFont(font)
        self.string9.setObjectName("string9")
        self.group9.addWidget(self.string9)
        self.cooldown9 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(False)
        font.setWeight(50)
        self.cooldown9.setFont(font)
        self.cooldown9.setObjectName("cooldown9")
        self.group9.addWidget(self.cooldown9)
        self.group9.setStretch(1, 10)
        self.verticalLayout.addLayout(self.group9)
        self.minimizeButton = QtWidgets.QPushButton(self.centralWidget)
        self.minimizeButton.setGeometry(QtCore.QRect(880, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.minimizeButton.setFont(font)
        self.minimizeButton.setStyleSheet("")
        self.minimizeButton.setObjectName("minimizeButton")
        self.closeButton = QtWidgets.QPushButton(self.centralWidget)
        self.closeButton.setGeometry(QtCore.QRect(920, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("")
        self.closeButton.setObjectName("closeButton")
        self.title = QtWidgets.QLabel(self.centralWidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setObjectName("title")
        ProfileEditWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(ProfileEditWindow)
        QtCore.QMetaObject.connectSlotsByName(ProfileEditWindow)

    def retranslateUi(self, ProfileEditWindow):
        _translate = QtCore.QCoreApplication.translate
        ProfileEditWindow.setWindowTitle(_translate("ProfileEditWindow", "Редактирование профиля"))
        self.createProfileButton.setText(_translate("ProfileEditWindow", "Действие"))
        self.shortcutlabel.setText(_translate("ProfileEditWindow", "Клавиша"))
        self.profiileNameLabel.setText(_translate("ProfileEditWindow", " Название профиля"))
        self.label1.setText(_translate("ProfileEditWindow", "1"))
        self.cooldown1.setText(_translate("ProfileEditWindow", "0"))
        self.label2.setText(_translate("ProfileEditWindow", "2"))
        self.cooldown2.setText(_translate("ProfileEditWindow", "0"))
        self.label3.setText(_translate("ProfileEditWindow", "3"))
        self.cooldown3.setText(_translate("ProfileEditWindow", "0"))
        self.label4.setText(_translate("ProfileEditWindow", "4"))
        self.cooldown4.setText(_translate("ProfileEditWindow", "0"))
        self.label5.setText(_translate("ProfileEditWindow", "5"))
        self.cooldown5.setText(_translate("ProfileEditWindow", "0"))
        self.label6.setText(_translate("ProfileEditWindow", "6"))
        self.cooldown6.setText(_translate("ProfileEditWindow", "0"))
        self.label7.setText(_translate("ProfileEditWindow", "7"))
        self.cooldown7.setText(_translate("ProfileEditWindow", "0"))
        self.label8.setText(_translate("ProfileEditWindow", "8"))
        self.cooldown8.setText(_translate("ProfileEditWindow", "0"))
        self.label9.setText(_translate("ProfileEditWindow", "9"))
        self.cooldown9.setText(_translate("ProfileEditWindow", "0"))
        self.minimizeButton.setText(_translate("ProfileEditWindow", "_"))
        self.closeButton.setText(_translate("ProfileEditWindow", "X"))
        self.title.setText(_translate("ProfileEditWindow", "Редактирование"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProfileEditWindow = QtWidgets.QMainWindow()
    ui = Ui_ProfileEditWindow()
    ui.setupUi(ProfileEditWindow)
    ProfileEditWindow.show()
    sys.exit(app.exec())
