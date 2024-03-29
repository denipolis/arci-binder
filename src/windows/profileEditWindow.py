# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profileEditWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QKeySequenceEdit, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_ProfileEditWindow(object):
    def setupUi(self, ProfileEditWindow):
        if not ProfileEditWindow.objectName():
            ProfileEditWindow.setObjectName(u"ProfileEditWindow")
        ProfileEditWindow.resize(961, 500)
        icon = QIcon()
        icon.addFile(u":/resources/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        ProfileEditWindow.setWindowIcon(icon)
        ProfileEditWindow.setStyleSheet(u"QLineEdit {\n"
"    background-color: #13171c;\n"
"	border: 2px solid #cfcfcf;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QKeySequenceEdit {\n"
"    background-color: #13171c;\n"
"	border: 2px solid #cfcfcf;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QWidget {\n"
"   color: #f5f5f5;\n"
"   font-family:  Rubik SemiBold;\n"
"   font-size: 13px;\n"
"}\n"
"\n"
"QListWidget {\n"
"   background-color: #13171c;\n"
"	border: 2px solid #cfcfcf;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1d2024;\n"
"	border: none;\n"
" 	border-collapse: separate;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #222a33;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: #1d2329;\n"
"}")
        self.mainWidget = QWidget(ProfileEditWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.createProfileButton = QPushButton(self.mainWidget)
        self.createProfileButton.setObjectName(u"createProfileButton")
        self.createProfileButton.setGeometry(QRect(420, 460, 181, 31))
        font = QFont()
        font.setFamilies([u"Rubik SemiBold"])
        self.createProfileButton.setFont(font)
        self.createProfileButton.setStyleSheet(u"border-radius: 6px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.createProfileButton.setIcon(icon1)
        self.createProfileButton.setIconSize(QSize(18, 18))
        self.shortcutlabel = QLabel(self.mainWidget)
        self.shortcutlabel.setObjectName(u"shortcutlabel")
        self.shortcutlabel.setGeometry(QRect(540, 410, 91, 16))
        self.shortcutlabel.setFont(font)
        self.shortcutlabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220)\n"
"}")
        self.shortcutlabel.setAlignment(Qt.AlignCenter)
        self.hotkey = QKeySequenceEdit(self.mainWidget)
        self.hotkey.setObjectName(u"hotkey")
        self.hotkey.setGeometry(QRect(540, 430, 91, 21))
        self.hotkey.setFont(font)
        self.profileName = QLineEdit(self.mainWidget)
        self.profileName.setObjectName(u"profileName")
        self.profileName.setGeometry(QRect(330, 430, 181, 21))
        self.profileNameLabel = QLabel(self.mainWidget)
        self.profileNameLabel.setObjectName(u"profileNameLabel")
        self.profileNameLabel.setGeometry(QRect(330, 410, 181, 16))
        self.profileNameLabel.setFont(font)
        self.profileNameLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220)\n"
"}")
        self.profileNameLabel.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.mainWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 60, 921, 341))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.group1 = QHBoxLayout()
        self.group1.setSpacing(10)
        self.group1.setObjectName(u"group1")
        self.group1.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label1 = QLabel(self.verticalLayoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setEnabled(True)
        self.label1.setFont(font)
        self.label1.setAlignment(Qt.AlignCenter)

        self.group1.addWidget(self.label1)

        self.string1 = QLineEdit(self.verticalLayoutWidget)
        self.string1.setObjectName(u"string1")
        self.string1.setFont(font)

        self.group1.addWidget(self.string1)

        self.cooldown1 = QLineEdit(self.verticalLayoutWidget)
        self.cooldown1.setObjectName(u"cooldown1")
        self.cooldown1.setFont(font)
        self.cooldown1.setInputMethodHints(Qt.ImhDigitsOnly)

        self.group1.addWidget(self.cooldown1)

        self.group1.setStretch(1, 10)

        self.verticalLayout.addLayout(self.group1)

        self.group2 = QHBoxLayout()
        self.group2.setSpacing(10)
        self.group2.setObjectName(u"group2")
        self.group2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label2 = QLabel(self.verticalLayoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignCenter)

        self.group2.addWidget(self.label2)

        self.string2 = QLineEdit(self.verticalLayoutWidget)
        self.string2.setObjectName(u"string2")
        self.string2.setFont(font)

        self.group2.addWidget(self.string2)

        self.cooldown2 = QLineEdit(self.verticalLayoutWidget)
        self.cooldown2.setObjectName(u"cooldown2")
        self.cooldown2.setFont(font)
        self.cooldown2.setInputMethodHints(Qt.ImhDigitsOnly)

        self.group2.addWidget(self.cooldown2)

        self.group2.setStretch(1, 10)

        self.verticalLayout.addLayout(self.group2)

        self.group3 = QHBoxLayout()
        self.group3.setSpacing(10)
        self.group3.setObjectName(u"group3")
        self.group3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label3 = QLabel(self.verticalLayoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setFont(font)
        self.label3.setAlignment(Qt.AlignCenter)

        self.group3.addWidget(self.label3)

        self.string3 = QLineEdit(self.verticalLayoutWidget)
        self.string3.setObjectName(u"string3")
        self.string3.setFont(font)

        self.group3.addWidget(self.string3)

        self.cooldown3 = QLineEdit(self.verticalLayoutWidget)
        self.cooldown3.setObjectName(u"cooldown3")
        self.cooldown3.setFont(font)
        self.cooldown3.setInputMethodHints(Qt.ImhDigitsOnly)

        self.group3.addWidget(self.cooldown3)

        self.group3.setStretch(1, 10)

        self.verticalLayout.addLayout(self.group3)

        self.group4 = QHBoxLayout()
        self.group4.setSpacing(10)
        self.group4.setObjectName(u"group4")
        self.group4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label4 = QLabel(self.verticalLayoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setFont(font)
        self.label4.setAlignment(Qt.AlignCenter)

        self.group4.addWidget(self.label4)

        self.string4 = QLineEdit(self.verticalLayoutWidget)
        self.string4.setObjectName(u"string4")
        self.string4.setFont(font)

        self.group4.addWidget(self.string4)

        self.cooldown4 = QLineEdit(self.verticalLayoutWidget)
        self.cooldown4.setObjectName(u"cooldown4")
        self.cooldown4.setFont(font)
        self.cooldown4.setInputMethodHints(Qt.ImhDigitsOnly)

        self.group4.addWidget(self.cooldown4)

        self.group4.setStretch(1, 10)

        self.verticalLayout.addLayout(self.group4)

        self.group5 = QHBoxLayout()
        self.group5.setSpacing(10)
        self.group5.setObjectName(u"group5")
        self.group5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label5 = QLabel(self.verticalLayoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setFont(font)
        self.label5.setAlignment(Qt.AlignCenter)

        self.group5.addWidget(self.label5)

        self.string5 = QLineEdit(self.verticalLayoutWidget)
        self.string5.setObjectName(u"string5")
        self.string5.setFont(font)

        self.group5.addWidget(self.string5)

        self.cooldown5 = QLineEdit(self.verticalLayoutWidget)
        self.cooldown5.setObjectName(u"cooldown5")
        self.cooldown5.setFont(font)
        self.cooldown5.setInputMethodHints(Qt.ImhDigitsOnly)

        self.group5.addWidget(self.cooldown5)

        self.group5.setStretch(1, 10)

        self.verticalLayout.addLayout(self.group5)

        self.group6 = QHBoxLayout()
        self.group6.setSpacing(10)
        self.group6.setObjectName(u"group6")
        self.group6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label6 = QLabel(self.verticalLayoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setFont(font)
        self.label6.setAlignment(Qt.AlignCenter)

        self.group6.addWidget(self.label6)

        self.string6 = QLineEdit(self.verticalLayoutWidget)
        self.string6.setObjectName(u"string6")
        self.string6.setFont(font)

        self.group6.addWidget(self.string6)

        self.cooldown6 = QLineEdit(self.verticalLayoutWidget)
        self.cooldown6.setObjectName(u"cooldown6")
        self.cooldown6.setFont(font)

        self.group6.addWidget(self.cooldown6)

        self.group6.setStretch(1, 10)

        self.verticalLayout.addLayout(self.group6)

        self.group7 = QHBoxLayout()
        self.group7.setSpacing(10)
        self.group7.setObjectName(u"group7")
        self.group7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label7 = QLabel(self.verticalLayoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setFont(font)
        self.label7.setAlignment(Qt.AlignCenter)

        self.group7.addWidget(self.label7)

        self.string7 = QLineEdit(self.verticalLayoutWidget)
        self.string7.setObjectName(u"string7")
        self.string7.setFont(font)

        self.group7.addWidget(self.string7)

        self.cooldown7 = QLineEdit(self.verticalLayoutWidget)
        self.cooldown7.setObjectName(u"cooldown7")
        self.cooldown7.setFont(font)

        self.group7.addWidget(self.cooldown7)

        self.group7.setStretch(1, 10)

        self.verticalLayout.addLayout(self.group7)

        self.group8 = QHBoxLayout()
        self.group8.setSpacing(10)
        self.group8.setObjectName(u"group8")
        self.group8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label8 = QLabel(self.verticalLayoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setFont(font)
        self.label8.setAlignment(Qt.AlignCenter)

        self.group8.addWidget(self.label8)

        self.string8 = QLineEdit(self.verticalLayoutWidget)
        self.string8.setObjectName(u"string8")
        self.string8.setFont(font)

        self.group8.addWidget(self.string8)

        self.cooldown8 = QLineEdit(self.verticalLayoutWidget)
        self.cooldown8.setObjectName(u"cooldown8")
        self.cooldown8.setFont(font)

        self.group8.addWidget(self.cooldown8)

        self.group8.setStretch(1, 10)

        self.verticalLayout.addLayout(self.group8)

        self.group9 = QHBoxLayout()
        self.group9.setSpacing(10)
        self.group9.setObjectName(u"group9")
        self.group9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label9 = QLabel(self.verticalLayoutWidget)
        self.label9.setObjectName(u"label9")
        self.label9.setFont(font)
        self.label9.setAlignment(Qt.AlignCenter)

        self.group9.addWidget(self.label9)

        self.string9 = QLineEdit(self.verticalLayoutWidget)
        self.string9.setObjectName(u"string9")
        self.string9.setFont(font)

        self.group9.addWidget(self.string9)

        self.cooldown9 = QLineEdit(self.verticalLayoutWidget)
        self.cooldown9.setObjectName(u"cooldown9")
        self.cooldown9.setFont(font)

        self.group9.addWidget(self.cooldown9)

        self.group9.setStretch(1, 10)

        self.verticalLayout.addLayout(self.group9)

        self.closeButton = QPushButton(self.mainWidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(920, 10, 31, 31))
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.title = QLabel(self.mainWidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 10, 181, 31))
        self.title.setFont(font)
        self.rowLabel = QLabel(self.mainWidget)
        self.rowLabel.setObjectName(u"rowLabel")
        self.rowLabel.setGeometry(QRect(30, 50, 61, 16))
        self.rowLabel.setFont(font)
        self.cooldownLabel = QLabel(self.mainWidget)
        self.cooldownLabel.setObjectName(u"cooldownLabel")
        self.cooldownLabel.setGeometry(QRect(810, 50, 81, 16))
        self.cooldownLabel.setFont(font)
        self.label = QLabel(self.mainWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 961, 501))
        self.label.setStyleSheet(u"background-color: #13171c;\n"
"border-radius: 15px;")
        ProfileEditWindow.setCentralWidget(self.mainWidget)
        self.label.raise_()
        self.createProfileButton.raise_()
        self.shortcutlabel.raise_()
        self.hotkey.raise_()
        self.profileName.raise_()
        self.profileNameLabel.raise_()
        self.verticalLayoutWidget.raise_()
        self.closeButton.raise_()
        self.title.raise_()
        self.rowLabel.raise_()
        self.cooldownLabel.raise_()

        self.retranslateUi(ProfileEditWindow)

        QMetaObject.connectSlotsByName(ProfileEditWindow)
    # setupUi

    def retranslateUi(self, ProfileEditWindow):
        ProfileEditWindow.setWindowTitle(QCoreApplication.translate("ProfileEditWindow", u"ArciBinder - \u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440", None))
        self.createProfileButton.setText(QCoreApplication.translate("ProfileEditWindow", u" \u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.shortcutlabel.setText(QCoreApplication.translate("ProfileEditWindow", u"\u041a\u043b\u0430\u0432\u0438\u0448\u0430", None))
#if QT_CONFIG(tooltip)
        self.hotkey.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.hotkey.setKeySequence("")
        self.profileName.setText("")
        self.profileNameLabel.setText(QCoreApplication.translate("ProfileEditWindow", u" \u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0444\u0438\u043b\u044f", None))
        self.label1.setText(QCoreApplication.translate("ProfileEditWindow", u"1", None))
        self.string1.setText("")
        self.cooldown1.setText(QCoreApplication.translate("ProfileEditWindow", u"0", None))
        self.label2.setText(QCoreApplication.translate("ProfileEditWindow", u"2", None))
        self.cooldown2.setText(QCoreApplication.translate("ProfileEditWindow", u"0", None))
        self.label3.setText(QCoreApplication.translate("ProfileEditWindow", u"3", None))
        self.cooldown3.setText(QCoreApplication.translate("ProfileEditWindow", u"0", None))
        self.label4.setText(QCoreApplication.translate("ProfileEditWindow", u"4", None))
        self.cooldown4.setText(QCoreApplication.translate("ProfileEditWindow", u"0", None))
        self.label5.setText(QCoreApplication.translate("ProfileEditWindow", u"5", None))
        self.cooldown5.setText(QCoreApplication.translate("ProfileEditWindow", u"0", None))
        self.label6.setText(QCoreApplication.translate("ProfileEditWindow", u"6", None))
        self.cooldown6.setText(QCoreApplication.translate("ProfileEditWindow", u"0", None))
        self.label7.setText(QCoreApplication.translate("ProfileEditWindow", u"7", None))
        self.cooldown7.setText(QCoreApplication.translate("ProfileEditWindow", u"0", None))
        self.label8.setText(QCoreApplication.translate("ProfileEditWindow", u"8", None))
        self.cooldown8.setText(QCoreApplication.translate("ProfileEditWindow", u"0", None))
        self.label9.setText(QCoreApplication.translate("ProfileEditWindow", u"9", None))
        self.cooldown9.setText(QCoreApplication.translate("ProfileEditWindow", u"0", None))
        self.closeButton.setText("")
        self.title.setText(QCoreApplication.translate("ProfileEditWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440", None))
        self.rowLabel.setText(QCoreApplication.translate("ProfileEditWindow", u"\u0422\u0435\u043a\u0441\u0442", None))
        self.cooldownLabel.setText(QCoreApplication.translate("ProfileEditWindow", u"\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430", None))
        self.label.setText("")
    # retranslateUi

