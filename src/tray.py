from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu
import os
import utils

basedir = os.path.dirname(__file__)

def createTray(self):
  self.trayicon = QSystemTrayIcon(self)
  self.trayicon.setIcon(QIcon(os.path.join(basedir, "ui/images/logo32x32.png")))
  trayShowAction = QAction("Открыть", icon=QIcon(QIcon(os.path.join(basedir, "ui/images/show.png"))), parent=self)
  trayQuitAction = QAction("Выйти", icon=QIcon(QIcon(os.path.join(basedir, "ui/images/cross.png"))), parent=self)

  trayShowAction.triggered.connect(lambda: self.show())
  trayQuitAction.triggered.connect(lambda: utils.quit())

  traymenu = QMenu()
  trayTitle = traymenu.addAction("ArciBinder")
  trayTitle.setEnabled(False)
  traymenu.addSeparator()
  traymenu.addAction(trayShowAction)
  traymenu.addAction(trayQuitAction)

  self.trayicon.setContextMenu(traymenu)
  self.trayicon.show()