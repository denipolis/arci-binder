import sys

import uuid as uuidlib
import os

import utils

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QIcon, QMouseEvent, QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog

from windows.mainWindow import Ui_MainWindow
from windows.profileEditWindow import Ui_ProfileEditWindow

from tray import TrayIcon
from database import Database
from binder import Binder
from config import Config
from updater import Updater
from abpHandler import ABPHandler
from typing import Callable
from enum import Enum
import windows.resources_rc

if not os.path.exists(os.path.join(os.getenv('APPDATA'), 'arcibinder')):
    os.makedirs(os.path.join(os.getenv('APPDATA'), 'arcibinder'))

basedir = os.path.dirname(__file__)

database = Database(os.path.join(os.getenv('APPDATA'), 'arcibinder', 'arcibinder.db'))
binder = Binder(database)
updater = Updater()
config = Config()
profileReader = ABPHandler(database)
app = QApplication(sys.argv)

class ProfileEditWindow(QMainWindow):
    def rebuildUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.createProfileButton.clicked.connect(lambda: self.createProfileButtonCallback())
        self.ui.closeButton.clicked.connect(lambda: ( self.hide(), mainWindow.show() ))
        self.ui.hotkey.keySequenceChanged.connect(lambda: self.ui.hotkey.setKeySequence(self.ui.hotkey.keySequence().toString().split(',')[0]) if self.ui.hotkey.keySequence().count() > 1 else None)
        
    def __init__(self):
        super(ProfileEditWindow, self).__init__()
        self.ui = Ui_ProfileEditWindow()
        self.rebuildUI()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.show: Callable[[str], None] = lambda uuid = None : ( self.rebuildUI(), self.__showWithUuid(uuid) )

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
            self.ui.hotkey.setKeySequence(profileHotkey)

            for i in range(0, len(profileStrings)):
                currentRowString = getattr(editWindow.ui, f'string{i+1}')
                currentRowCooldown = getattr(editWindow.ui, f'cooldown{i+1}')

                if profileStrings[i][0] != "":
                    currentRowString.setText(profileStrings[i][0])
                    currentRowCooldown.setText(str(profileStrings[i][1])) 
        else:
            self.uuid = uuidlib.uuid4().hex
            self.ui.createProfileButton.setText('Создать')

    def createProfileButtonCallback(self):
        if not self.ui.profileName.text():
            QMessageBox(QMessageBox.Icon.Critical, "Создание профиля", "Вы забыли ввести название профиля!", QMessageBox.StandardButton.Ok).exec()
            return

        hotkey = self.ui.hotkey.keySequence().toString().split(',')[0]
        profileWithHotkey = database.findProfileByHotkey(hotkey)
        
        if database.isProfileExistsByUuid(self.uuid):
            database.deleteProfile(self.uuid)

        if database.isProfileExistsByHotkey(hotkey):
            QMessageBox(QMessageBox.Icon.Critical, "Создание профиля", f"Выбранная клавиша уже занята!\nУдалите профиль \"{profileWithHotkey[0]}\" или измените клавишу.", QMessageBox.StandardButton.Ok).exec()
            return

        database.createProfile(self.ui.profileName.text(), self.uuid, hotkey)

        for i in range(1, 10):
            currentRowString = getattr(self.ui, f'string{i}').text()
            currentRowCooldown = getattr(self.ui, f'cooldown{i}').text()
            if currentRowString != "" and currentRowCooldown != "" and currentRowCooldown.isnumeric():
                database.addStringToProfile(self.uuid, currentRowString, int(currentRowCooldown))

        binder.updateProfiles()
        mainWindow.show()
        self.hide()

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
        self.ui.deleteProfileButton.clicked.connect(lambda: self.deleteButtonCallback())
        self.ui.loadProfileButton.clicked.connect(lambda: self.loadButtonCallback())
        self.ui.editProfileButton.clicked.connect(lambda: editWindow.show(database.findUuidByName(self.ui.listWidget.currentItem().text())))

        self.ui.adButton.clicked.connect(lambda: utils.openURL("https://github.com/denipolis/arci-binder/"))

        self.ui.closeButton.clicked.connect(lambda: self.closeButtonCallback())
        self.ui.minimizeButton.clicked.connect(lambda: self.closeButtonCallback())
        self.ui.profilesButton.clicked.connect(lambda: self.changeWidget(MainMenuType.PROFILES))
        self.ui.settingsButton.clicked.connect(lambda: self.changeWidget(MainMenuType.SETTINGS))

        self.ui.reloadBinderButton.clicked.connect(lambda: binder.updateProfiles())
        self.ui.exportProfilesButton.clicked.connect(lambda: self.exportButtonCallback())

        self.ui.listWidget.clear()
        self.ui.listWidget.clicked.connect(lambda: self.handleListWidgetClick())

        self.ui.trayCheckbox.setChecked(database.isSettingEnabled('hideInTray'))
        self.ui.trayCheckbox.stateChanged.connect(lambda state: database.setSettingValue('hideInTray', state))

        self.ui.autorunCheckbox.setChecked(utils.isAutoRun())
        self.ui.autorunCheckbox.stateChanged.connect(lambda state: utils.enableAutoRun() if state == 2 else utils.disableAutoRun())

        self.ui.nameCheckbox.setChecked(database.isSettingEnabled('checkFullScreen'))
        self.ui.nameCheckbox.stateChanged.connect(lambda state: database.setSettingValue('checkFullScreen', state))
        
        self.ui.updateCheckbox.setChecked(database.isSettingEnabled('dontCheckForUpdates'))
        self.ui.updateCheckbox.stateChanged.connect(lambda state: database.setSettingValue('dontCheckForUpdates', state))

        for profile in database.findAllProfiles():
            self.ui.listWidget.addItem(profile[0])

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui = Ui_MainWindow()
        self.rebuildUI()
        self.show = lambda: ( self.rebuildUI(), self.showNormal() )
    
    def handleListWidgetClick(self):
        self.ui.editProfileButton.setDisabled(self.ui.listWidget.currentItem() == None)
        self.ui.deleteProfileButton.setDisabled(self.ui.listWidget.currentItem() == None)

    def loadButtonCallback(self):
        fileDialog = QFileDialog()
        fileDialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        fileDialog.setNameFilter("ArciBinder Profiles (*.abp)")
        fileDialog.setWindowTitle("Выберите профиль (.abp), который хотите импортировать")
        fileDialog.exec()

        profileReader.loadProfileByPath(fileDialog.selectedFiles()[0])
        self.rebuildUI()
        binder.updateProfiles()

    def exportButtonCallback(self):
        fileDialog = QFileDialog()
        fileDialog.setFileMode(QFileDialog.FileMode.Directory)
        fileDialog.setWindowTitle("Выберите папку, куда экспортировать профили")
        fileDialog.exec()

        profileReader.exportAllProfilesInFolder(fileDialog.selectedFiles()[0])

    def createButtonCallback(self):
        self.hide()
        editWindow.show()

    def closeButtonCallback(self):
        if not database.isSettingEnabled('hideInTray'):
            utils.quit()

        self.hide()
        
        trayIcon.showMessage("ArciBinder", "Биндер работает в фоновом режиме. Его можно найти в трее.", QIcon(u":/icons/images/logo32x32.png"), 1500)
        
    def deleteButtonCallback(self):
        answer = QMessageBox(QMessageBox.Icon.Question, "Удаление профиля", f"Вы действительно хотите удалить профиль \"{self.ui.listWidget.currentItem().text()}\"?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No).exec()

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

    app.setApplicationName(f'ArciBinder {config.getVersion()}')
    app.setApplicationDisplayName(f'ArciBinder {config.getVersion()}')
    app.setApplicationVersion(config.getVersion())
    app.setWindowIcon(QIcon(u":/icons/images/logo32x32.png"))
    if QFontDatabase.addApplicationFont(u":/fonts/fonts/Rubik-SemiBold.ttf") < 0: print('Unable to load font!')
    
    mainWindow.show()

    if updater.isUpdateAvailable() and not database.isSettingEnabled('dontCheckForUpdates'):
        answer = QMessageBox(QMessageBox.Icon.Information, "Обновление", f"С момента последнего запуска было найдено новое обновление.\nНажмите \"Да\", если хотите перейти на страницу для скачивания!", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No).exec()
        if answer == QMessageBox.StandardButton.Yes:
            utils.openURL('https://github.com/denipolis/arci-binder/releases/')

    sys.exit(app.exec())

if __name__ == "__main__":
    main()