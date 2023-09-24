# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(605, 427)
        MainWindow.setStyleSheet(u"QWidget {\n"
"   background-color: #13171c;\n"
"   color: #f5f5f5;\n"
"   font-family:  Rubik;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 2px solid #cfcfcf;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1d2024;\n"
"	border: none;\n"
" 	border-collapse: separate;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"    background-color: #202024;\n"
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
"	border: 2px solid #cfcfcf;\n"
"	border-radius: 7px;\n"
"}")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.mainWidget = QWidget(MainWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setStyleSheet(u"")
        self.closeButton = QPushButton(self.mainWidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(560, 10, 31, 31))
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(11)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet(u"")
        self.minimizeButton = QPushButton(self.mainWidget)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setGeometry(QRect(520, 10, 31, 31))
        self.minimizeButton.setFont(font)
        self.minimizeButton.setStyleSheet(u"")
        self.navigationWidget = QWidget(self.mainWidget)
        self.navigationWidget.setObjectName(u"navigationWidget")
        self.navigationWidget.setGeometry(QRect(0, 0, 61, 431))
        self.navigationWidget.setStyleSheet(u"QWidget {\n"
"   background-color: #586675;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"   background-color: #505d6b;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"   background-color: #44515e;\n"
"}")
        self.profilesButton = QPushButton(self.navigationWidget)
        self.profilesButton.setObjectName(u"profilesButton")
        self.profilesButton.setGeometry(QRect(10, 50, 41, 41))
        self.settingsButton = QPushButton(self.navigationWidget)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setGeometry(QRect(10, 100, 41, 41))
        self.title = QLabel(self.navigationWidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 0, 61, 51))
        font1 = QFont()
        font1.setFamilies([u"Rubik"])
        font1.setPointSize(14)
        self.title.setFont(font1)
        self.title.setLayoutDirection(Qt.LeftToRight)
        self.title.setStyleSheet(u"color: #ffffff;")
        self.title.setAlignment(Qt.AlignCenter)
        self.adButton = QPushButton(self.navigationWidget)
        self.adButton.setObjectName(u"adButton")
        self.adButton.setGeometry(QRect(0, 400, 61, 21))
        self.adButton.setStyleSheet(u"")
        self.settingsWidget = QWidget(self.mainWidget)
        self.settingsWidget.setObjectName(u"settingsWidget")
        self.settingsWidget.setEnabled(True)
        self.settingsWidget.setGeometry(QRect(60, 0, 541, 431))
        self.settingsWidget.setStyleSheet(u"")
        self.settingsTitle = QLabel(self.settingsWidget)
        self.settingsTitle.setObjectName(u"settingsTitle")
        self.settingsTitle.setGeometry(QRect(10, 10, 111, 31))
        font2 = QFont()
        font2.setFamilies([u"Rubik"])
        font2.setPointSize(12)
        self.settingsTitle.setFont(font2)
        self.trayCheckbox = QCheckBox(self.settingsWidget)
        self.trayCheckbox.setObjectName(u"trayCheckbox")
        self.trayCheckbox.setGeometry(QRect(10, 50, 511, 21))
        font3 = QFont()
        font3.setFamilies([u"Rubik"])
        font3.setPointSize(10)
        self.trayCheckbox.setFont(font3)
        self.autorunCheckbox = QCheckBox(self.settingsWidget)
        self.autorunCheckbox.setObjectName(u"autorunCheckbox")
        self.autorunCheckbox.setGeometry(QRect(10, 70, 511, 21))
        self.autorunCheckbox.setFont(font3)
        self.nameCheckbox = QCheckBox(self.settingsWidget)
        self.nameCheckbox.setObjectName(u"nameCheckbox")
        self.nameCheckbox.setGeometry(QRect(10, 90, 511, 21))
        self.nameCheckbox.setFont(font3)
        self.profilesWidget = QWidget(self.mainWidget)
        self.profilesWidget.setObjectName(u"profilesWidget")
        self.profilesWidget.setEnabled(True)
        self.profilesWidget.setGeometry(QRect(60, 0, 541, 431))
        self.profilesWidget.setStyleSheet(u"")
        self.createProfileButton = QPushButton(self.profilesWidget)
        self.createProfileButton.setObjectName(u"createProfileButton")
        self.createProfileButton.setGeometry(QRect(470, 80, 60, 60))
        self.createProfileButton.setFont(font1)
        self.createProfileButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.createProfileButton.setIcon(icon)
        self.createProfileButton.setIconSize(QSize(48, 48))
        self.editProfileButton = QPushButton(self.profilesWidget)
        self.editProfileButton.setObjectName(u"editProfileButton")
        self.editProfileButton.setEnabled(False)
        self.editProfileButton.setGeometry(QRect(470, 150, 60, 60))
        self.editProfileButton.setFont(font1)
        self.editProfileButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editProfileButton.setIcon(icon1)
        self.editProfileButton.setIconSize(QSize(48, 48))
        self.deleteProfileButton = QPushButton(self.profilesWidget)
        self.deleteProfileButton.setObjectName(u"deleteProfileButton")
        self.deleteProfileButton.setEnabled(False)
        self.deleteProfileButton.setGeometry(QRect(470, 220, 60, 60))
        self.deleteProfileButton.setFont(font1)
        self.deleteProfileButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteProfileButton.setIcon(icon2)
        self.deleteProfileButton.setIconSize(QSize(48, 48))
        self.profilesTitle = QLabel(self.profilesWidget)
        self.profilesTitle.setObjectName(u"profilesTitle")
        self.profilesTitle.setGeometry(QRect(10, 10, 101, 31))
        self.profilesTitle.setFont(font2)
        self.listWidget = QListWidget(self.profilesWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QRect(20, 80, 431, 321))
        self.listWidget.setStyleSheet(u"")
        self.label = QLabel(self.profilesWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 111, 16))
        self.label.setFont(font3)
        self.listWidget.raise_()
        self.createProfileButton.raise_()
        self.editProfileButton.raise_()
        self.deleteProfileButton.raise_()
        self.profilesTitle.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.mainWidget)
        self.settingsWidget.raise_()
        self.profilesWidget.raise_()
        self.minimizeButton.raise_()
        self.closeButton.raise_()
        self.navigationWidget.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.minimizeButton.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.profilesButton.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"AB", None))
        self.adButton.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.settingsTitle.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.trayCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u044f\u0442\u0430\u0442\u044c \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0432 \u0442\u0440\u0435\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 \"\u0417\u0430\u043a\u0440\u044b\u0442\u044c\"", None))
        self.autorunCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a\u0430\u0442\u044c \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0432\u043c\u0435\u0441\u0442\u0435 \u0441 \u0441\u0438\u0441\u0442\u0435\u043c\u043e\u0439 (\u0430\u0432\u0442\u043e\u0437\u0430\u043f\u0443\u0441\u043a)", None))
        self.nameCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0431\u0438\u043d\u0434\u044b \u043d\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u0432 RAGE Multiplayer", None))
        self.createProfileButton.setText("")
        self.editProfileButton.setText("")
        self.deleteProfileButton.setText("")
        self.profilesTitle.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448\u0438 \u043f\u0440\u043e\u0444\u0438\u043b\u0438:", None))
    # retranslateUi

