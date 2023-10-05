import configparser
import urllib.request
import json

class Updater():
  def __init__(self):
    pass

  def isUpdateAvailable(self):
    config = configparser.ConfigParser()
    config.read('config')

    currentVersion = config['Build']['Version']

    with urllib.request.urlopen('https://api.github.com/repos/denipolis/arci-binder/releases/latest') as response:
      response = json.loads(response.read())
      versionOnGitHub = response['tag_name']

      if currentVersion != versionOnGitHub:
        return True
    
    return False