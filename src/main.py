import sys

import uuid as uuidlib
import os

import utils

from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QIcon, QMouseEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from mainWindow import Ui_MainWindow
from profileEditWindow import Ui_ProfileEditWindow
from profileDeleteWindow import Ui_ProfileDeleteWindow
from profileListWindow import Ui_ProfileListWindow

from tray import TrayIcon
from database import Database
from binder import Binder

from typing import Callable
from enum import Enum

if not os.path.exists(os.path.join(os.getenv('APPDATA'), 'arcibinder')):
    os.makedirs(os.path.join(os.getenv('APPDATA'), 'arcibinder'))

basedir = os.path.dirname(__file__)

database = Database(os.path.join(os.getenv('APPDATA'), 'arcibinder', 'arcibinder.db'))
binder = Binder(database)
app = QApplication(sys.argv)

class ProfileListWindow(QMainWindow):
    def rebuildUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.editProfileButton.clicked.connect(lambda: self.editProfileButtonCallback())
        self.ui.closeButton.clicked.connect(lambda: self.hide())
        self.ui.minimizeButton.clicked.connect(lambda: self.hide())
        self.ui.listWidget.clear()

        for profile in database.findAllProfiles():
            self.ui.listWidget.addItem(profile[0])

    def __init__(self):
        super(ProfileListWindow, self).__init__()
        self.ui = Ui_ProfileListWindow()
        self.rebuildUI()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show = lambda: (self.rebuildUI(), self.showNormal())

    def editProfileButtonCallback(self):

        if not self.ui.listWidget.currentItem():
            return

        editWindow.show(database.findUuidByName(self.ui.listWidget.currentItem().text()))
    
    def closeEvent(self, event) -> None:
        event.ignore()
        self.hide()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.previousPosition = event.globalPosition()
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        delta = QPointF(event.globalPosition() - self.previousPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.previousPosition = event.globalPosition()

listWindow = ProfileListWindow()

class ProfileEditWindow(QMainWindow):
    def rebuildUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.createProfileButton.clicked.connect(lambda: self.createProfileButtonCallback())
        self.ui.closeButton.clicked.connect(lambda: self.hide())
        self.ui.minimizeButton.clicked.connect(lambda: self.hide())
        
    def __init__(self):
        super(ProfileEditWindow, self).__init__()
        self.ui = Ui_ProfileEditWindow()
        self.rebuildUI()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show: Callable[[str], None] = lambda uuid : (self.rebuildUI(), self.__showWithUuid(uuid))

    def __showWithUuid(self, uuid: str) -> None:
        self.showNormal()
        self.rebuildUI()

        if uuid: # when editing
            profileStrings = database.findStringsInProfile(uuid)
            profileHotkey = database.findHotkeyByUuid(uuid)
            profileName = database.findProfileByUuid(uuid)[0]

            self.uuid = uuid

            self.ui.createProfileButton.setText('Изменить')
            self.ui.profileName.setText(profileName)
            self.ui.shortcut.setKeySequence(profileHotkey)

            for i in range(0, len(profileStrings)):
                currentRowString = getattr(editWindow.ui, f'string{i+1}')
                currentRowCooldown = getattr(editWindow.ui, f'cooldown{i+1}')

                if profileStrings[i][0] != "":
                    currentRowString.setText(profileStrings[i][0])
                    currentRowCooldown.setText(str(profileStrings[i][1])) 
        else:
            self.uuid = uuidlib.uuid4().hex

    def createProfileButtonCallback(self):
        if not self.ui.profileName.text():
            msgbox = QMessageBox()
            msgbox.setWindowTitle(f"ArciBinder")
            msgbox.setText(f"Вы забыли ввести название профиля!")
            msgbox.setIcon(QMessageBox.Icon.Critical)
            msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgbox.exec()
            return

        hotkey = self.ui.shortcut.keySequence().toString().split(',')[0]
        profileWithHotkey = database.findProfileByHotkey(hotkey)
        
        if database.isProfileExistsByUuid(self.uuid):
            database.deleteProfile(self.uuid)

        if database.isProfileExistsByHotkey(hotkey):
            msgbox = QMessageBox()
            msgbox.setWindowTitle(f"ArciBinder")
            msgbox.setText(f"Данная клавиша уже занята!\nУдалите профиль \"{profileWithHotkey[0]}\" или измените клавишу.")
            msgbox.setIcon(QMessageBox.Icon.Critical)
            msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgbox.exec()
            return

        database.createProfile(self.ui.profileName.text(), self.uuid, hotkey)

        for i in range(1, 10):
            currentRowString = getattr(self.ui, f'string{i}').text()
            currentRowCooldown = getattr(self.ui, f'cooldown{i}').text()
            if currentRowString != "" and currentRowCooldown != "" and currentRowCooldown.isnumeric():
                database.addStringToProfile(self.uuid, currentRowString, int(currentRowCooldown))

        binder.updateProfiles()
        self.hide()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.previousPosition = event.globalPosition()
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        delta = QPointF(event.globalPosition() - self.previousPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.previousPosition = event.globalPosition()

editWindow = ProfileEditWindow()

class ProfileDeleteWindow(QMainWindow):
    def rebuildUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.deleteProfileButton.clicked.connect(lambda:  self.deleteButtonCallback())
        self.ui.closeButton.clicked.connect(lambda: self.hide())
        self.ui.minimizeButton.clicked.connect(lambda: self.hide())
        self.ui.listWidget.clear()

        for profile in database.findAllProfiles():
            self.ui.listWidget.addItem(profile[0])

    def __init__(self):
        super(ProfileDeleteWindow, self).__init__()
        self.ui = Ui_ProfileDeleteWindow()
        self.rebuildUI()
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show = lambda: ( self.rebuildUI(), self.showNormal() )

    def deleteButtonCallback(self):
        msgbox = QMessageBox()
        msgbox.setText(f"Вы действительно хотите удалить профиль {self.ui.listWidget.currentItem().text()}?")
        msgbox.setWindowTitle(f"ArciBinder")
        msgbox.setIcon(QMessageBox.Icon.Question)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        answer = msgbox.exec()

        if answer == QMessageBox.StandardButton.Yes:
            try:
                database.deleteProfile(database.findUuidByName(self.ui.listWidget.currentItem().text()))
            except:
                pass

            binder.updateProfiles()
            self.ui.listWidget.takeItem(self.ui.listWidget.currentIndex().row())

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.previousPosition = event.globalPosition()
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        delta = QPointF(event.globalPosition() - self.previousPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.previousPosition = event.globalPosition()

deleteWindow = ProfileDeleteWindow()

class MainMenuType(Enum):
    PROFILES = 1
    SETTINGS = 2

class MainWindow(QMainWindow):
    def rebuildUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.newProfileButton.clicked.connect(lambda: editWindow.show())
        self.ui.deleteProfileButton.clicked.connect(lambda: self.deleteProfileCallback())
        self.ui.editProfileButton.clicked.connect(lambda: editWindow.show(database.findUuidByName(self.ui.listWidget.currentItem().text())))

        self.ui.adButton.clicked.connect(lambda: utils.openURL("https://github.com/denipolis"))

        self.ui.closeButton.clicked.connect(lambda: self.closeButtonCallback())
        self.ui.minimizeButton.clicked.connect(lambda: self.closeButtonCallback())
        self.ui.profilesButton.clicked.connect(lambda: self.changeWidget(MainMenuType.PROFILES))
        self.ui.settingsButton.clicked.connect(lambda: self.changeWidget(MainMenuType.SETTINGS))
        self.ui.listWidget.clear()

        for profile in database.findAllProfiles():
            self.ui.listWidget.addItem(profile[0])

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.rebuildUI()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint )
    
    def closeButtonCallback(self):
        self.hide()
        trayIcon.showMessage("ArciBinder", "Биндер работает в фоновом режиме. Его можно найти в трее.", msecs=1500)
        
    def deleteProfileCallback(self):
        msgbox = QMessageBox()
        msgbox.setText(f"Вы действительно хотите удалить профиль \"{self.ui.listWidget.currentItem().text()}\"?")
        msgbox.setWindowTitle(f"ArciBinder")
        msgbox.setIcon(QMessageBox.Icon.Question)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        answer = msgbox.exec()

        if answer == QMessageBox.StandardButton.Yes:
            try:
                database.deleteProfile(database.findUuidByName(self.ui.listWidget.currentItem().text()))
            except:
                pass

            binder.updateProfiles()
            self.ui.listWidget.takeItem(self.ui.listWidget.currentIndex().row())
    
    def changeWidget(self, type: MainMenuType):
        if type == MainMenuType.PROFILES:
            self.ui.settingsWidget.hide()
            self.ui.profilesWidget.show()
        if type == MainMenuType.SETTINGS:
            self.ui.settingsWidget.show()
            self.ui.profilesWidget.hide()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.previousPosition = event.globalPosition()
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        delta = QPointF(event.globalPosition() - self.previousPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.previousPosition = event.globalPosition()

mainWindow = MainWindow()

trayIcon = TrayIcon(mainWindow)

def main():
    database.initializeProfiles()
    binder.updateProfiles()

    app.setApplicationName('ArciBinder')
    app.setApplicationDisplayName('ArciBinder')
    app.setApplicationVersion('1.1.1')
    app.setWindowIcon(QIcon(os.path.join(basedir, "ui/images/logo.ico")))

    mainWindow.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()