import sqlite3
import os

class Database:
  def __init__(self, pathToFile):
    self.database = sqlite3.connect(pathToFile, check_same_thread = False)
    self.cursor = self.database.cursor()
  
  def initializeProfiles(self):
    try: self.cursor.execute('''CREATE TABLE profilesData
            (name text, uuid text, hotkey text)
            ''')
    except:
        pass
    
  def findNameByUuid(self, uuid) -> str:
    self.cursor.execute(f"SELECT name FROM profilesData WHERE uuid='{uuid}'")
    return str(self.cursor.fetchone()[0])
  
  def findUuidByName(self, name) -> str:
    self.cursor.execute(f"SELECT uuid FROM profilesData WHERE name='{name}'")
    return str(self.cursor.fetchone()[0])
  
  def findHotkeyByUuid(self, uuid) -> str:
    self.cursor.execute(f"SELECT hotkey FROM profilesData WHERE uuid='{uuid}'")
    return self.cursor.fetchone()[0]

  def findAllProfiles(self) -> str:
    self.cursor.execute(f'SELECT * FROM profilesData')
    return self.cursor.fetchall()
  
  def findStringsInProfile(self, uuid) -> str:
    self.cursor.execute(f'SELECT * FROM profile_{uuid}')
    return self.cursor.fetchall()
  
  def findProfileByHotkey(self, hotkey) -> str:
    self.cursor.execute(f"SELECT * FROM profilesData WHERE hotkey='{hotkey}'")
    return self.cursor.fetchall()

  def deleteProfile(self, uuid) -> None:
    self.cursor.execute(f"DELETE FROM 'profilesData' WHERE uuid='{uuid}'")
    self.cursor.execute(f"DROP TABLE 'profile_{uuid}'")
    self.database.commit()

  def createProfile(self, name, uuid, hotkey) -> None:
    self.cursor.execute(f'''
            CREATE TABLE profile_{uuid}
            (message text, cooldown int)
        ''')
    self.cursor.execute(f'''INSERT INTO profilesData VALUES('{name}', '{uuid}', '{hotkey}')''')


    self.database.commit()

  def addStringToProfile(self, uuid, string, cooldown) -> None:
    self.cursor.execute(f'''INSERT INTO 'profile_{uuid}' VALUES('{string}', '{cooldown}')''')
    self.database.commit()