import sqlite3
import os

class Database:
  def __init__(self, pathToFile):
    self.database = sqlite3.connect(pathToFile, check_same_thread = False)
    self.cursor = self.database.cursor()
    self.initialize()
  
  def initialize(self):
    try:
      self.cursor.execute('''CREATE TABLE settings
          (key text, value integer)
          ''')
      self.cursor.execute('''CREATE TABLE profilesData
          (name text, uuid text, hotkey text)
           ''')
    except:
        pass
  
  
  def isSettingExists(self, key: str) -> bool:
    self.cursor.execute(f"SELECT * FROM settings WHERE key='{key}'")
    return self.cursor.fetchone() != None
  
  def isSettingEnabled(self, key: str) -> bool:
    if not self.isSettingExists(key):
      return False

    self.cursor.execute(f"SELECT * FROM settings WHERE key='{key}'")
    return True if int(self.cursor.fetchone()[1]) == 2 else False
  
  def setSettingValue(self, key: str, value: int) -> None:
    if value != 2 and value != 0:
      return

    if self.isSettingExists(key):
      self.cursor.execute(f"UPDATE settings SET value='{value}' WHERE key='{key}'")
    else:
      self.cursor.execute(f"INSERT INTO settings VALUES('{key}', '{value}')")
    
    self.database.commit()

  def findNameByUuid(self, uuid: str) -> str:
    self.cursor.execute(f"SELECT name FROM profilesData WHERE uuid='{uuid}'")
    return str(self.cursor.fetchone()[0])
  
  def findUuidByName(self, name: str) -> str:
    self.cursor.execute(f"SELECT uuid FROM profilesData WHERE name='{name}'")
    return str(self.cursor.fetchone()[0])
  
  def findHotkeyByUuid(self, uuid: str) -> str:
    self.cursor.execute(f"SELECT hotkey FROM profilesData WHERE uuid='{uuid}'")
    return self.cursor.fetchone()[0]

  def findAllProfiles(self):
    self.cursor.execute(f'SELECT * FROM profilesData')
    return self.cursor.fetchall()
  
  def findStringsInProfile(self, uuid: str):
    self.cursor.execute(f'SELECT * FROM profile_{uuid}')
    return self.cursor.fetchall()
  
  def findProfileByHotkey(self, hotkey: str):
    self.cursor.execute(f"SELECT * FROM profilesData WHERE hotkey='{hotkey}'")
    return self.cursor.fetchone()
  
  def findProfileByUuid(self, uuid: str):
    self.cursor.execute(f"SELECT * FROM profilesData WHERE uuid='{uuid}'")
    return self.cursor.fetchone()

  def deleteProfile(self, uuid: str) -> None:
    self.cursor.execute(f"DELETE FROM profilesData WHERE uuid='{uuid}'")
    self.cursor.execute(f"DROP TABLE profile_{uuid}")
    self.database.commit()

  def isProfileExistsByUuid(self, uuid: str) -> bool:
    self.cursor.execute(f"SELECT * FROM profilesData WHERE uuid='{uuid}'")
    return self.cursor.fetchone() != None
  
  def isProfileExistsByHotkey(self, hotkey: str) -> bool:
    self.cursor.execute(f"SELECT * FROM profilesData WHERE hotkey='{hotkey}'")
    return self.cursor.fetchone() != None

  def createProfile(self, name: str, uuid: str, hotkey: str) -> None:
    self.cursor.execute(f'''
            CREATE TABLE profile_{uuid}
            (message text, cooldown int)
        ''')
    self.cursor.execute(f'''INSERT INTO profilesData VALUES('{name}', '{uuid}', '{hotkey}')''')
    self.database.commit()

  def addStringToProfile(self, uuid: str, string: str, cooldown: int) -> None:
    self.cursor.execute(f'''INSERT INTO 'profile_{uuid}' VALUES('{string}', '{cooldown}')''')
    self.database.commit()