import time
import utils
import keyboard
from database import Database

class Binder:
  def __init__(self, database: Database) -> None:
    self.database = database
    pass

    
  def updateProfiles(self):
    profiles = self.database.findAllProfiles()

    try:
        keyboard.clear_all_hotkeys() 
    except:
        pass

    for profile in profiles:
        if not profile[2]:
            return

        keyboard.add_hotkey(profile[2], self.playProfile, args=(str(profile[1]),))

  def playProfile(self, profileName: str):
    print(utils.getActiveWindowTitle().find("RAGE Multiplayer"))
    if self.database.isSettingEnabled('dontCheckForName') or "RAGE Multiplayer" in utils.getActiveWindowTitle():
      profileStrings = self.database.findStringsInProfile(profileName)

      for profileString in profileStrings:
          time.sleep(float(profileString[1])/1000)
          utils.singleKeyPress("T")
          keyboard.write(str(profileString[0]))
          utils.singleKeyPress("ENTER")