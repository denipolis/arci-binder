from turtle import width
from imports import *
import os
from tray import createTray
from database import Database

appIconPath = 'images/logo.png'

if not os.path.exists(os.path.join(os.getenv('APPDATA'), 'arcibinder')):
    os.makedirs(os.path.join(os.getenv('APPDATA'), 'arcibinder'))

basedir = os.path.dirname(__file__)

database = Database(os.path.join(os.getenv('APPDATA'), 'arcibinder', 'arcibinder.db'))
app = QApplication(sys.argv)
        
global listWindow
global mainWindow
global editWindow
global deleteWindow

def updateProfiles():
    profiles = database.findAllProfiles()

    try:
        keyboard.clear_all_hotkeys() 
    except:
        pass

    for profile in profiles:
        if not profile[2]:
            return

        keyboard.add_hotkey(profile[2], playProfile, args=(str(profile[1]),))


class ProfileListWindow(QMainWindow):
    def rebuildUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.editProfileButton.clicked.connect(lambda: self.editProfileButtonCallback())
        self.ui.closeButton.clicked.connect(lambda: self.hide())
        self.ui.minimizeButton.clicked.connect(lambda: self.hide())

    def __init__(self):
        super(ProfileListWindow, self).__init__()
        self.ui = Ui_ProfileListWindow()
        self.rebuildUI()
        self.updateListItems()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    def _show(self):
        self.rebuildUI()
        self.updateListItems()
        self.show()

    def editProfileButtonCallback(self):
        global editWindow

        if not self.ui.listWidget.currentItem():
            return

        editWindow.showWithUuid(database.findUuidByName(self.ui.listWidget.currentItem().text()))

    def updateListItems(self):
        self.ui.listWidget.clear()

        for profile in database.findAllProfiles():
            self.ui.listWidget.addItem(profile[0])
    
    def closeEvent(self, event) -> None:
        event.ignore()
        self.hide()


class ProfileEditWindow(QMainWindow):
    saveduuid = -1
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
    
    def _show(self):
        self.saveduuid = -1
        self.rebuildUI()
        self.show()

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
            # stupid method of getting any objects in self.ui
            if currentRowString != "" and currentRowCooldown != "" and currentRowCooldown.isnumeric():
                database.addStringToProfile(_uuid, currentRowString, int(currentRowCooldown))

        updateProfiles()
        self.rebuildUI()
        self.hide()

class ProfileDeleteWindow(QMainWindow):
    def rebuildUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.deleteProfileButton.clicked.connect(lambda:  self.deleteButtonCallback())
        self.ui.closeButton.clicked.connect(lambda: self.hide())
        self.ui.minimizeButton.clicked.connect(lambda: self.hide())
        self.updateListItems()

    def __init__(self):
        super(ProfileDeleteWindow, self).__init__()
        self.ui = Ui_ProfileDeleteWindow()
        self.rebuildUI()
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    def _show(self):
        self.rebuildUI()
        self.updateListItems()
        self.show()

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

            updateProfiles()
            self.ui.listWidget.takeItem(self.ui.listWidget.currentIndex().row())

    def updateListItems(self):
        self.ui.listWidget.clear()

        for profile in database.findAllProfiles():
            self.ui.listWidget.addItem(profile[0])

class MainWindow(QMainWindow):
    def rebuildUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.createProfileButton.clicked.connect(lambda: editWindow._show())
        self.ui.deleteProfileButton.clicked.connect(lambda: deleteWindow._show())
        self.ui.editProfileButton.clicked.connect(lambda: listWindow._show())

        self.ui.adButton.clicked.connect(lambda: utils.openLink("https://github.com/denipolis"))

        self.ui.closeButton.clicked.connect(lambda: self.closeButtonCallback())
        self.ui.minimizeButton.clicked.connect(lambda: self.closeButtonCallback())

    def __init__(self):
        super(MainWindow, self).__init__()
        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")
        self.ui = Ui_MainWindow()
        self.rebuildUI()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        createTray(self)
    
    def closeButtonCallback(self):
        self.hide()
        self.trayicon.showMessage("ArciBinder", "Биндер работает в фоновом режиме. Его можно найти в трей-меню.", msecs=2000)
        

def playProfile(profileName: str):
    if not utils.getActiveWindowTitle().find("RAGE Multiplayer"):
        return

    profileStrings = database.findStringsInProfile(profileName)

    for profileString in profileStrings:
        time.sleep(float(profileString[1])/1000)
        utils.singleKeyPress("T")
        keyboard.write(str(profileString[0]))
        utils.singleKeyPress("ENTER")

def main():
    database.initializeProfiles()
    updateProfiles()

    global mainWindow, editWindow, deleteWindow, listWindow

    app.setWindowIcon(QIcon(os.path.join(basedir, "images/logo.ico")))

    mainWindow = MainWindow()
    editWindow = ProfileEditWindow()
    deleteWindow = ProfileDeleteWindow()
    listWindow = ProfileListWindow()

    mainWindow.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()