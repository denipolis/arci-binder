from database import Database

from PySide6.QtWidgets import QMessageBox
from patterns.singleton import Singleton
import json
import os
import uuid as uuidlib

class ABPHandler(metaclass=Singleton):
  def __init__(self, database: Database):
    self.database = database
    pass

  def exportAllProfilesInFolder(self, path):
    for profile in self.database.findAllProfiles():
      structurizedProfile = {
        'name': profile[0],
        'hotkey': profile[2],
        'strings': self.database.findStringsInProfile(profile[1])
      }

      file = open(os.path.join(path, f"{profile[0]}.abp"), 'w', -1, "utf-8")
      file.writelines(json.dumps(structurizedProfile, ensure_ascii=False))
      

  def loadProfileByPath(self, path) -> bool:
    loadedProfile = open(path, 'r', -1, 'utf-8')
    parsedProfile = json.loads(loadedProfile.read())
    
    if not parsedProfile['name']:
      QMessageBox(QMessageBox.Icon.Critical, "ArciBinder", "Найдена ошибка в данных профиля. К сожалению, его невозможно загрузить.\nОшибка: не найдено секции name", QMessageBox.StandardButton.Ok).exec()
      return False
    
    if not parsedProfile['hotkey']:
      QMessageBox(QMessageBox.Icon.Critical, "ArciBinder", "Найдена ошибка в данных профиля. К сожалению, его невозможно загрузить.\nОшибка: не найдено секции hotkey", QMessageBox.StandardButton.Ok).exec()
      return False

    if not parsedProfile['strings']:
      QMessageBox(QMessageBox.Icon.Critical, "ArciBinder", "Найдена ошибка в данных профиля. К сожалению, его невозможно загрузить.\nОшибка: не найдено секции strings", QMessageBox.StandardButton.Ok).exec()
      return False
    
    if len(parsedProfile['strings']) > 9:
      QMessageBox(QMessageBox.Icon.Critical, "ArciBinder", "Найдена ошибка в данных профиля. К сожалению, его невозможно загрузить.\nОшибка: слишком много элементов в strings (>9)", QMessageBox.StandardButton.Ok).exec()
      return False
    
    if(self.database.isProfileExistsByHotkey(parsedProfile['hotkey'])):
      QMessageBox(QMessageBox.Icon.Critical, "ArciBinder", f"Горячую клавишу \"{parsedProfile['hotkey']}\" уже использует профиль \"{self.database.findProfileByHotkey(parsedProfile['hotkey'])[0]}.\nУдалите его или поменяйте горячую клавишу, что бы загрузить новый профиль.", QMessageBox.StandardButton.Ok).exec()
      return False

    if(self.database.isProfileExistsByHotkey(parsedProfile['name'])):
      QMessageBox(QMessageBox.Icon.Critical, "ArciBinder", f"Название \"{parsedProfile['hotkey']}\" уже используется.\nИзмените название прошлому профилю, что бы загрузить новый.", QMessageBox.StandardButton.Ok).exec()
      return False

    profileUuid = uuidlib.uuid4().hex

    self.database.createProfile(parsedProfile['name'], profileUuid, parsedProfile['hotkey'])

    for string in parsedProfile['strings']:
      self.database.addStringToProfile(profileUuid, str(string[0]), int(string[1]))

    QMessageBox(QMessageBox.Icon.Information, "ArciBinder", f"Профиль {parsedProfile['name']} успешно загружен!", QMessageBox.StandardButton.Ok).exec()
    return True