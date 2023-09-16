# Form implementation generated from reading ui file 'ui/mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(352, 140)
        MainWindow.setStyleSheet("QWidget {\n"
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
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.createProfileButton = QtWidgets.QPushButton(self.centralwidget)
        self.createProfileButton.setGeometry(QtCore.QRect(50, 40, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        self.createProfileButton.setFont(font)
        self.createProfileButton.setStyleSheet("")
        self.createProfileButton.setObjectName("createProfileButton")
        self.deleteProfileButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteProfileButton.setGeometry(QtCore.QRect(180, 40, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.deleteProfileButton.setFont(font)
        self.deleteProfileButton.setStyleSheet("")
        self.deleteProfileButton.setObjectName("deleteProfileButton")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.title.setStyleSheet("QLabel {\n"
"    color: rgb(220, 220, 220)\n"
"}")
        self.title.setObjectName("title")
        self.editProfileButton = QtWidgets.QPushButton(self.centralwidget)
        self.editProfileButton.setGeometry(QtCore.QRect(80, 70, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.editProfileButton.setFont(font)
        self.editProfileButton.setStyleSheet("")
        self.editProfileButton.setObjectName("editProfileButton")
        self.adButton = QtWidgets.QPushButton(self.centralwidget)
        self.adButton.setGeometry(QtCore.QRect(100, 100, 161, 20))
        self.adButton.setStyleSheet("QPushButton:pressed {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: #c9c9c9;\n"
"}")
        self.adButton.setObjectName("adButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(320, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("color: #fffde0;")
        self.closeButton.setObjectName("closeButton")
        self.minimizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.minimizeButton.setGeometry(QtCore.QRect(290, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.minimizeButton.setFont(font)
        self.minimizeButton.setStyleSheet("color: #fffde0;\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #ff0000;\n"
"}")
        self.minimizeButton.setObjectName("minimizeButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action2 = QtGui.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName("action_3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        self.createProfileButton.setText(_translate("MainWindow", "Создать профиль"))
        self.deleteProfileButton.setText(_translate("MainWindow", "Удалить профиль"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p>ArciBinder</p></body></html>"))
        self.editProfileButton.setText(_translate("MainWindow", "Редактировать профили"))
        self.adButton.setText(_translate("MainWindow", "Github разработчика"))
        self.closeButton.setText(_translate("MainWindow", "X"))
        self.minimizeButton.setText(_translate("MainWindow", "_"))
        self.action.setText(_translate("MainWindow", "Сбросить базу данных"))
        self.action2.setText(_translate("MainWindow", "Выйти"))
        self.action_3.setText(_translate("MainWindow", "пон"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())