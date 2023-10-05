from config import Config
import urllib.request
import json

class Updater():
  def __init__(self):
    self._config = Config()
    pass

  def isUpdateAvailable(self):
    with urllib.request.urlopen('https://api.github.com/repos/denipolis/arci-binder/releases/latest') as response:
      response = json.loads(response.read())
      versionOnGitHub = response['tag_name']

      if self._config.getVersion() != versionOnGitHub:
        return True
    
    return False