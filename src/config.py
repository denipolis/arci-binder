import os
import configparser
from patterns.singleton import Singleton

class Config(metaclass=Singleton):
  _config = configparser.ConfigParser()

  def __init__(self):
    self._config.read(os.path.join(os.getcwd(), 'config'))
  
  def getVersion(self):
    try:
      return self._config['Build']['Version']
    except:
      return '0.0'