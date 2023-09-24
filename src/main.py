import sys

import uuid as uuidlib
import os

import utils

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QIcon, QMouseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QCheckBox

from windows.mainWindow import Ui_MainWindow
from windows.profileEditWindow import Ui_ProfileEditWindow

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

class ProfileEditWindow(QMainWindow):
    def rebuildUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.createProfileButton.clicked.connect(lambda: self.createProfileButtonCallback())
        self.ui.closeButton.clicked.connect(lambda: ( self.hide(), mainWindow.show() ))
        self.ui.minimizeButton.clicked.connect(lambda: self.hide())
        
    def __init__(self):
        super(ProfileEditWindow, self).__init__()
        self.ui = Ui_ProfileEditWindow()
        self.rebuildUI()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show: Callable[[str], None] = lambda uuid=None : (self.rebuildUI(), self.__showWithUuid(uuid))

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
            QMessageBox(QMessageBox.Icon.Critical, "ArciBinder", "Вы забыли ввести название профиля!", QMessageBox.StandardButton.Ok).exec()
            return

        hotkey = self.ui.shortcut.keySequence().toString().split(',')[0]
        profileWithHotkey = database.findProfileByHotkey(hotkey)
        
        if database.isProfileExistsByUuid(self.uuid):
            database.deleteProfile(self.uuid)

        if database.isProfileExistsByHotkey(hotkey):
            QMessageBox(QMessageBox.Icon.Critical, "ArciBinder", f"Выбранная клавиша уже занята!\nУдалите профиль \"{profileWithHotkey[0]}\" или измените клавишу.", QMessageBox.StandardButton.Ok).exec()
            return

        database.createProfile(self.ui.profileName.text(), self.uuid, hotkey)

        for i in range(1, 10):
            currentRowString = getattr(self.ui, f'string{i}').text()
            currentRowCooldown = getattr(self.ui, f'cooldown{i}').text()
            if currentRowString != "" and currentRowCooldown != "" and currentRowCooldown.isnumeric():
                database.addStringToProfile(self.uuid, currentRowString, int(currentRowCooldown))

        binder.updateProfiles()
        self.hide()
        mainWindow.show()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.previousPosition = event.globalPosition()
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        delta = QPointF(event.globalPosition() - self.previousPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.previousPosition = event.globalPosition()

editWindow = ProfileEditWindow()

class MainMenuType(Enum):
    PROFILES = 1
    SETTINGS = 2

class MainWindow(QMainWindow):
    def rebuildUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.createProfileButton.clicked.connect(lambda: self.createButtonCallback())
        self.ui.deleteProfileButton.clicked.connect(lambda: self.deleteProfileCallback())
        self.ui.editProfileButton.clicked.connect(lambda: editWindow.show(database.findUuidByName(self.ui.listWidget.currentItem().text())))

        self.ui.adButton.clicked.connect(lambda: utils.openURL("https://github.com/denipolis"))

        self.ui.closeButton.clicked.connect(lambda: self.closeButtonCallback())
        self.ui.minimizeButton.clicked.connect(lambda: self.closeButtonCallback())
        self.ui.profilesButton.clicked.connect(lambda: self.changeWidget(MainMenuType.PROFILES))
        self.ui.settingsButton.clicked.connect(lambda: self.changeWidget(MainMenuType.SETTINGS))

        self.ui.listWidget.clear()
        self.ui.listWidget.clicked.connect(lambda: self.handleListWidgetClick())

        self.ui.trayCheckbox.setChecked(database.isSettingEnabled('hideInTray'))
        self.ui.trayCheckbox.stateChanged.connect(lambda state: database.setSettingValue('hideInTray', state))

        self.ui.autorunCheckbox.setChecked(utils.isAutoRun())
        self.ui.autorunCheckbox.stateChanged.connect(lambda state: utils.enableAutoRun() if state == 2 else utils.disableAutoRun())

        self.ui.nameCheckbox.setChecked(database.isSettingEnabled('dontCheckForName'))
        self.ui.nameCheckbox.stateChanged.connect(lambda state: database.setSettingValue('dontCheckForName', state))

        for profile in database.findAllProfiles():
            self.ui.listWidget.addItem(profile[0])

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.rebuildUI()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show = lambda: ( self.rebuildUI(), self.showNormal() )
    
    def handleListWidgetClick(self):
        self.ui.editProfileButton.setDisabled(self.ui.listWidget.currentItem() == None)
        self.ui.deleteProfileButton.setDisabled(self.ui.listWidget.currentItem() == None)

    def createButtonCallback(self):
        self.hide()
        editWindow.show()

    def closeButtonCallback(self):
        if not database.isSettingEnabled('hideInTray'):
            utils.quit()

        self.hide()
        
        trayIcon.showMessage("ArciBinder", "Биндер работает в фоновом режиме. Его можно найти в трее.", msecs=1500)
        
    def deleteProfileCallback(self):
        answer = QMessageBox(QMessageBox.Icon.Question, "ArciBinder", f"Вы действительно хотите удалить профиль \"{self.ui.listWidget.currentItem().text()}\"?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No).exec()

        if answer == QMessageBox.StandardButton.Yes:
            database.deleteProfile(database.findUuidByName(self.ui.listWidget.currentItem().text()))

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
    binder.updateProfiles()

    app.setApplicationName('ArciBinder')
    app.setApplicationDisplayName('ArciBinder')
    app.setApplicationVersion('1.2')
    app.setWindowIcon(QIcon(os.path.join(basedir, "ui/images/logo.ico")))

    mainWindow.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()