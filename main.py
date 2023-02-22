from turtle import width
from imports import *
import os

appIconPath = 'images/logo.png'

if not os.path.exists(os.path.join(os.getenv('APPDATA'), 'arcibinder')):
    os.makedirs(os.path.join(os.getenv('APPDATA'), 'arcibinder'))

db = sqlite3.connect(os.path.join(os.getenv('APPDATA'), 'arcibinder', 'arcibinder.db'), check_same_thread = False)
dbcursor = db.cursor()

basedir = os.path.dirname(__file__)

def initDB():
    try: dbcursor.execute('''CREATE TABLE profilesData
            (name text, uuid text, hotkey text)
            ''')
    except:
        pass

def clearDB():
    msgbox = QMessageBox()
    msgbox.setText(f"Вы действительно хотите сбросить базу данных?\nУдалятся все профили, настройки и другие данные биндера.")
    msgbox.setWindowTitle(f"ArciBinder")
    msgbox.setIcon(QMessageBox.Icon.Warning)
    msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

    answer = msgbox.exec()

    if answer == QMessageBox.StandardButton.Yes:
        try:
            db.close()
            os.remove("arcibinder.db")
            essentials.quit()
        except:
            pass

app = QApplication(sys.argv)
        
global profilesList
global listWindow
global mainWindow
global editWindow
global deleteWindow

def uuidToName(uuid: str) -> str:
    dbcursor.execute(f"SELECT name FROM profilesData WHERE uuid='{uuid}'")
    return str(dbcursor.fetchone()[0])

def nameToUuid(name: str) -> str:
    dbcursor.execute(f"SELECT uuid FROM profilesData WHERE name='{name}'")
    return str(dbcursor.fetchone()[0])
def updateProfiles():
    global profilesList

    dbcursor.execute(f'SELECT * FROM profilesData')
    profilesList = dbcursor.fetchall()

    print(f"LISTING PROFILES:\n\tList: {profilesList}")

    try:
        keyboard.clear_all_hotkeys() 
    except:
        pass

    for profile in profilesList:
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

        editWindow.showWithUuid(nameToUuid(self.ui.listWidget.currentItem().text()))

    def updateListItems(self):
        self.ui.listWidget.clear()

        for profile in profilesList:
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
        dbcursor.execute(f"SELECT * FROM 'profile_{uuid}'")
        profilestrings = dbcursor.fetchall()

        dbcursor.execute(f"SELECT hotkey FROM profilesData WHERE uuid='{uuid}'")
        hotkey = dbcursor.fetchone()[0]


        #self.ui.shortcut.hide()
        #self.ui.shortcutlabel.hide()
        self.ui.profileName.hide()
        self.ui.profiileNameLabel.hide()
        self.ui.createProfileButton.setText('Изменить')

        try:
            self.ui.shortcut.setKeySequence(hotkey)

            if profilestrings[0] != "":
                editWindow.ui.string1.setText(profilestrings[0][0])
                editWindow.ui.cooldown1.setText(str(profilestrings[0][1]))
                
            if profilestrings[1] != "":
                editWindow.ui.string2.setText(profilestrings[1][0])
                editWindow.ui.cooldown2.setText(str(profilestrings[1][1]))
                
            if profilestrings[2] != "":
                editWindow.ui.string3.setText(profilestrings[2][0])
                editWindow.ui.cooldown3.setText(str(profilestrings[2][1]))
                
            if profilestrings[3] != "":
                editWindow.ui.string4.setText(profilestrings[3][0])
                editWindow.ui.cooldown4.setText(str(profilestrings[3][1]))
                
            if profilestrings[4] != "":
                editWindow.ui.string5.setText(profilestrings[4][0])
                editWindow.ui.cooldown5.setText(str(profilestrings[4][1]))
                
            if profilestrings[5] != "":
                editWindow.ui.string6.setText(profilestrings[5][0])
                editWindow.ui.cooldown6.setText(str(profilestrings[5][1]))
                
            if profilestrings[6] != "":
                editWindow.ui.string7.setText(profilestrings[6][0])
                editWindow.ui.cooldown7.setText(str(profilestrings[6][1]))
                
            if profilestrings[7] != "":
                editWindow.ui.string8.setText(profilestrings[7][0])
                editWindow.ui.cooldown8.setText(str(profilestrings[7][1]))
                
            if profilestrings[8] != "":
                editWindow.ui.string9.setText(profilestrings[8][0])
                editWindow.ui.cooldown9.setText(str(profilestrings[8][1]))
        except:
            pass

    def createProfileButtonCallback(self):
        _uuid = self.saveduuid if self.saveduuid != -1 else str(uuid.uuid4().hex)
        _name = uuidToName(self.saveduuid) if self.saveduuid != -1 else self.ui.profileName.text()

        if not _name:
            msgbox = QMessageBox()
            msgbox.setWindowTitle(f"ArciBinder")
            msgbox.setText(f"Вы забыли ввести название профиля!")
            msgbox.setIcon(QMessageBox.Icon.Critical)
            msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgbox.exec()
            return

        dbcursor.execute(f"SELECT hotkey FROM profilesData WHERE uuid='{self.saveduuid}'")

        _hotkey = self.ui.shortcut.keySequence().toString().split(',')[0]

        dbcursor.execute(f"SELECT * FROM profilesData WHERE hotkey='{_hotkey}'")
        profileWithCurrentHotkey = dbcursor.fetchall()

        print(self.saveduuid == -1)

        if len(profileWithCurrentHotkey) > 0 and self.saveduuid == -1:
            msgbox = QMessageBox()
            msgbox.setWindowTitle(f"ArciBinder")
            msgbox.setText(f"Данная клавиша уже занята!\nУдалите профиль {profileWithCurrentHotkey[0][0]} или измените клавишу.")
            msgbox.setIcon(QMessageBox.Icon.Critical)
            msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgbox.exec()
            return

        if self.saveduuid != -1:
            dbcursor.execute(f"DROP TABLE profile_{_uuid}")
            dbcursor.execute(f"DELETE FROM 'profilesData' WHERE uuid='{_uuid}'")

        dbcursor.execute(f'''
            CREATE TABLE profile_{_uuid}
            (message text, cooldown int)
        ''')

        dbcursor.execute(f'''INSERT INTO profilesData VALUES('{_name}', '{_uuid}', '{_hotkey}') ''')

        if self.ui.string1.text() != "" and self.ui.cooldown1.text() != "" and self.ui.cooldown1.text().isnumeric(): dbcursor.execute(f'''INSERT INTO 'profile_{_uuid}' VALUES('{str(self.ui.string1.text())}', '{int(self.ui.cooldown1.text())}')''')
        if self.ui.string2.text() != "" and self.ui.cooldown2.text() != "" and self.ui.cooldown1.text().isnumeric(): dbcursor.execute(f'''INSERT INTO 'profile_{_uuid}' VALUES('{str(self.ui.string2.text())}', '{int(self.ui.cooldown2.text())}')''')
        if self.ui.string3.text() != "" and self.ui.cooldown3.text() != "" and self.ui.cooldown1.text().isnumeric(): dbcursor.execute(f'''INSERT INTO 'profile_{_uuid}' VALUES('{str(self.ui.string3.text())}', '{int(self.ui.cooldown3.text())}')''')
        if self.ui.string4.text() != "" and self.ui.cooldown4.text() != "" and self.ui.cooldown1.text().isnumeric(): dbcursor.execute(f'''INSERT INTO 'profile_{_uuid}' VALUES('{str(self.ui.string4.text())}', '{int(self.ui.cooldown4.text())}')''')
        if self.ui.string5.text() != "" and self.ui.cooldown5.text() != "" and self.ui.cooldown1.text().isnumeric(): dbcursor.execute(f'''INSERT INTO 'profile_{_uuid}' VALUES('{str(self.ui.string5.text())}', '{int(self.ui.cooldown5.text())}')''')
        if self.ui.string6.text() != "" and self.ui.cooldown6.text() != "" and self.ui.cooldown1.text().isnumeric(): dbcursor.execute(f'''INSERT INTO 'profile_{_uuid}' VALUES('{str(self.ui.string6.text())}', '{int(self.ui.cooldown6.text())}')''')
        if self.ui.string7.text() != "" and self.ui.cooldown7.text() != "" and self.ui.cooldown1.text().isnumeric(): dbcursor.execute(f'''INSERT INTO 'profile_{_uuid}' VALUES('{str(self.ui.string7.text())}', '{int(self.ui.cooldown7.text())}')''')
        if self.ui.string8.text() != "" and self.ui.cooldown8.text() != "" and self.ui.cooldown1.text().isnumeric(): dbcursor.execute(f'''INSERT INTO 'profile_{_uuid}' VALUES('{str(self.ui.string8.text())}', '{int(self.ui.cooldown8.text())}')''')
        if self.ui.string9.text() != "" and self.ui.cooldown9.text() != "" and self.ui.cooldown1.text().isnumeric(): dbcursor.execute(f'''INSERT INTO 'profile_{_uuid}' VALUES('{str(self.ui.string9.text())}', '{int(self.ui.cooldown9.text())}')''')
        #if self.ui.shortcut.keySequence().toString().split(',')[0] != "": dbcursor.execute(f'''INSERT INTO 'profilesData' VALUES('', '', '')''')
        
        db.commit()
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
                dbcursor.execute(f"DELETE FROM 'profilesData' WHERE name='{self.ui.listWidget.currentItem().text()}'")
                dbcursor.execute(f"DROP TABLE 'profile_{nameToUuid(self.ui.listWidget.currentItem().text())}'")
            except:
                pass

            db.commit()
            updateProfiles()
            self.updateListItems()

    def updateListItems(self):
        self.ui.listWidget.clear()

        for profile in profilesList:
            self.ui.listWidget.addItem(profile[0])

class MainWindow(QMainWindow):
    def makeTray(self):
        self.trayicon = QSystemTrayIcon(self)
        self.trayicon.setIcon(QIcon(os.path.join(basedir, "images/logo.png")))
        trayShowAction = QAction("Показать меню", icon=QIcon(QIcon(os.path.join(basedir, "images/show.png"))), parent=self)
        trayHideAction = QAction("Скрыть меню", icon=QIcon(QIcon(os.path.join(basedir, "images/hide.png"))), parent=self)
        trayDeleteProfilesAction = QAction("Удалить профили", icon=QIcon(QIcon(os.path.join(basedir, "images/trash-bin.png"))), parent=self)
        trayEditProfilesAction = QAction("Редактировать профили", icon=QIcon(QIcon(os.path.join(basedir, "images/edit.png"))), parent=self)
        trayQuitAction = QAction("Закрыть биндер", icon=QIcon(QIcon(os.path.join(basedir, "images/cross.png"))), parent=self)

        trayShowAction.triggered.connect(lambda: self.show())
        trayHideAction.triggered.connect(lambda: self.hide())
        trayQuitAction.triggered.connect(lambda: essentials.quit())
        trayDeleteProfilesAction.triggered.connect(lambda: deleteWindow._show())
        trayEditProfilesAction.triggered.connect(lambda: listWindow._show())

        traymenu = QMenu()
        trayTitle = traymenu.addAction("           ArciBinder")
        trayTitle.setEnabled(False)
        traymenu.addSeparator()
        traymenu.addAction(trayShowAction)
        traymenu.addAction(trayHideAction)
        traymenu.addSeparator()
        traymenu.addAction(trayDeleteProfilesAction)
        traymenu.addAction(trayEditProfilesAction)
        traymenu.addSeparator()
        traymenu.addAction(trayQuitAction)

        self.trayicon.setContextMenu(traymenu)
        self.trayicon.show()

    def rebuildUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.createProfileButton.clicked.connect(lambda: editWindow._show())
        self.ui.deleteProfileButton.clicked.connect(lambda: deleteWindow._show())
        self.ui.editProfileButton.clicked.connect(lambda: listWindow._show())

        self.ui.adButton.clicked.connect(lambda: essentials.openLink("https://github.com/denipolis"))

        self.ui.closeButton.clicked.connect(lambda: self.closeButtonCallback())
        self.ui.minimizeButton.clicked.connect(lambda: self.closeButtonCallback())

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.rebuildUI()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")
        self.makeTray()
    
    def closeButtonCallback(self):
        self.hide()
        self.trayicon.showMessage("ArciBinder", "Биндер работает в фоновом режиме. Его можно найти в трей-меню.", msecs=2000)
        

def playProfile(profilename: str):
    print(essentials.getActiveWindowTitle())
    if essentials.getActiveWindowTitle().find("RAGE Multiplayer") == False:
        return

    dbcursor.execute(f"SELECT * FROM 'profile_{profilename}'")
    profilestrings = dbcursor.fetchall()

    print(f"EXECUTING PROFILE: \n\tName: {profilename}.\n\tStrings: {profilestrings}")

    for profilestring in profilestrings:
        time.sleep(float(profilestring[1])/1000)
        essentials.singleKeyPress("T")
        keyboard.write(str(profilestring[0]))
        essentials.singleKeyPress("ENTER")

def main():
    initDB()
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