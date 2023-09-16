import sys

import uuid
import os

import utils

from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QIcon, QFontDatabase, QAction, QRegion, QMouseEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QSystemTrayIcon, QMenu, QWidgetAction, QLabel, QWidget

from mainWindow import Ui_MainWindow
from profileEditWindow import Ui_ProfileEditWindow
from profileDeleteWindow import Ui_ProfileDeleteWindow
from profileListWindow import Ui_ProfileListWindow

from tray import createTray
from database import Database
from binder import Binder

appIconPath = 'images/logo.png'

if not os.path.exists(os.path.join(os.getenv('APPDATA'), 'arcibinder')):
    os.makedirs(os.path.join(os.getenv('APPDATA'), 'arcibinder'))

basedir = os.path.dirname(__file__)

database = Database(os.path.join(os.getenv('APPDATA'), 'arcibinder', 'arcibinder.db'))
binder = Binder(database)
app = QApplication(sys.argv)
        
global listWindow
global mainWindow
global editWindow
global deleteWindow

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
        global editWindow

        if not self.ui.listWidget.currentItem():
            return

        editWindow.showWithUuid(database.findUuidByName(self.ui.listWidget.currentItem().text()))
    
    def closeEvent(self, event) -> None:
        event.ignore()
        self.hide()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.previousPosition = event.globalPosition()
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        delta = QPointF(event.globalPosition() - self.previousPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.previousPosition = event.globalPosition()


class ProfileEditWindow(QMainWindow):
    def rebuildUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.createProfileButton.clicked.connect(lambda: self.createProfileButtonCallback())
        self.ui.closeButton.clicked.connect(lambda: self.hide())
        self.ui.minimizeButton.clicked.connect(lambda: self.hide())
        self.saveduuid = -1
        
    def __init__(self):
        super(ProfileEditWindow, self).__init__()
        self.ui = Ui_ProfileEditWindow()
        self.rebuildUI()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show = lambda: (self.rebuildUI(), self.showNormal())

    def showWithUuid(self, uuid: str):
        self.saveduuid = uuid
        editWindow.show()
        self.rebuildUI()

        profileStrings = database.findStringsInProfile(uuid)
        hotkey = database.findHotkeyByUuid(uuid)

        self.ui.profileName.hide()
        self.ui.profiileNameLabel.hide()
        self.ui.createProfileButton.setText('Изменить')

        try:
            self.ui.shortcut.setKeySequence(hotkey)

            for i in range(0, 9):
                currentRowString = getattr(editWindow.ui, f'string{i+1}')
                currentRowCooldown = getattr(editWindow.ui, f'cooldown{i+1}')

                print(i, currentRowString)

                if profileStrings[i][0] != "":
                    currentRowString.setText(profileStrings[i][0])
                    currentRowCooldown.setText(str(profileStrings[i][1]))
        except Exception as e:
            print(profileStrings)
            pass

    def createProfileButtonCallback(self):
        _uuid = self.saveduuid if self.saveduuid != -1 else str(uuid.uuid4().hex)
        _name = database.findNameByUuid(self.saveduuid) if self.saveduuid != -1 else self.ui.profileName.text()

        if not _name:
            msgbox = QMessageBox()
            msgbox.setWindowTitle(f"ArciBinder")
            msgbox.setText(f"Вы забыли ввести название профиля!")
            msgbox.setIcon(QMessageBox.Icon.Critical)
            msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgbox.exec()
            return

        _hotkey = self.ui.shortcut.keySequence().toString().split(',')[0]

        profileWithHotkey = database.findProfileByHotkey(_hotkey)

        if len(profileWithHotkey) > 0 and self.saveduuid == -1:
            msgbox = QMessageBox()
            msgbox.setWindowTitle(f"ArciBinder")
            msgbox.setText(f"Данная клавиша уже занята!\nУдалите профиль {profileWithHotkey[0][0]} или измените клавишу.")
            msgbox.setIcon(QMessageBox.Icon.Critical)
            msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgbox.exec()
            return

        if self.saveduuid != -1:
            database.deleteProfile(_uuid)

        database.createProfile(_name, _uuid, _hotkey)

        for i in range(1, 10):
            currentRowString = getattr(self.ui, f'string{i}').text()
            currentRowCooldown = getattr(self.ui, f'cooldown{i}').text()
            if currentRowString != "" and currentRowCooldown != "" and currentRowCooldown.isnumeric():
                database.addStringToProfile(_uuid, currentRowString, int(currentRowCooldown))

        binder.updateProfiles()
        self.rebuildUI()
        self.hide()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.previousPosition = event.globalPosition()
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        delta = QPointF(event.globalPosition() - self.previousPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.previousPosition = event.globalPosition()

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


class MainWindow(QMainWindow):
    def rebuildUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.createProfileButton.clicked.connect(lambda: editWindow.show())
        self.ui.deleteProfileButton.clicked.connect(lambda: deleteWindow.show())
        self.ui.editProfileButton.clicked.connect(lambda: listWindow.show())

        self.ui.adButton.clicked.connect(lambda: utils.openLink("https://github.com/denipolis"))

        self.ui.closeButton.clicked.connect(lambda: self.closeButtonCallback())
        self.ui.minimizeButton.clicked.connect(lambda: self.closeButtonCallback())

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.rebuildUI()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        createTray(self)
    
    def closeButtonCallback(self):
        self.hide()
        self.trayicon.showMessage("ArciBinder", "Биндер работает в фоновом режиме. Его можно найти в трее.", msecs=1500)
        
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.previousPosition = event.globalPosition()
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        delta = QPointF(event.globalPosition() - self.previousPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.previousPosition = event.globalPosition()

def main():
    database.initializeProfiles()
    binder.updateProfiles()

    global mainWindow, editWindow, deleteWindow, listWindow

    app.setWindowIcon(QIcon(os.path.join(basedir, "ui/images/logo.ico")))

    mainWindow = MainWindow()
    editWindow = ProfileEditWindow()
    deleteWindow = ProfileDeleteWindow()
    listWindow = ProfileListWindow()

    mainWindow.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()