# Form implementation generated from reading ui file 'src/ui/profileDeleteWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProfileDeleteWindow(object):
    def setupUi(self, ProfileDeleteWindow):
        ProfileDeleteWindow.setObjectName("ProfileDeleteWindow")
        ProfileDeleteWindow.resize(378, 411)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ProfileDeleteWindow.setWindowIcon(icon)
        ProfileDeleteWindow.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(ProfileDeleteWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 361, 311))
        self.listWidget.setObjectName("listWidget")
        self.deleteProfileButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteProfileButton.setGeometry(QtCore.QRect(130, 360, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(14)
        self.deleteProfileButton.setFont(font)
        self.deleteProfileButton.setStyleSheet("border-radius: 7px;")
        self.deleteProfileButton.setObjectName("deleteProfileButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(340, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("color: #ffdbdc;")
        self.closeButton.setObjectName("closeButton")
        self.minimizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.minimizeButton.setGeometry(QtCore.QRect(310, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.minimizeButton.setFont(font)
        self.minimizeButton.setStyleSheet("color: #fffde0;")
        self.minimizeButton.setObjectName("minimizeButton")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 161, 21))
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
        ProfileDeleteWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ProfileDeleteWindow)
        self.statusbar.setObjectName("statusbar")
        ProfileDeleteWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(ProfileDeleteWindow)
        self.action.setObjectName("action")
        self.action2 = QtGui.QAction(ProfileDeleteWindow)
        self.action2.setObjectName("action2")
        self.action_3 = QtGui.QAction(ProfileDeleteWindow)
        self.action_3.setObjectName("action_3")

        self.retranslateUi(ProfileDeleteWindow)
        QtCore.QMetaObject.connectSlotsByName(ProfileDeleteWindow)

    def retranslateUi(self, ProfileDeleteWindow):
        _translate = QtCore.QCoreApplication.translate
        ProfileDeleteWindow.setWindowTitle(_translate("ProfileDeleteWindow", "Удаление профиля"))
        self.deleteProfileButton.setText(_translate("ProfileDeleteWindow", "Удалить"))
        self.closeButton.setText(_translate("ProfileDeleteWindow", "X"))
        self.minimizeButton.setText(_translate("ProfileDeleteWindow", "_"))
        self.title.setText(_translate("ProfileDeleteWindow", "<html><head/><body><p>Удаление профилей</p></body></html>"))
        self.action.setText(_translate("ProfileDeleteWindow", "Сбросить базу данных"))
        self.action2.setText(_translate("ProfileDeleteWindow", "Выйти"))
        self.action_3.setText(_translate("ProfileDeleteWindow", "Их нету"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProfileDeleteWindow = QtWidgets.QMainWindow()
    ui = Ui_ProfileDeleteWindow()
    ui.setupUi(ProfileDeleteWindow)
    ProfileDeleteWindow.show()
    sys.exit(app.exec())
