import sys

import sqlite3
import uuid
import keyboard
import time
import os

import essentials

from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFontDatabase, QAction, QRegion
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QSystemTrayIcon, QMenu, QWidgetAction, QLabel, QWidget

from mainWindow import Ui_MainWindow
from profileEditWindow import Ui_ProfileEditWindow
from profileDeleteWindow import Ui_ProfileDeleteWindow
from profileListWindow import Ui_ProfileListWindow