from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QSystemTrayIcon, QMenu
import os
import utils

import windows.resources_rc

basedir = os.path.dirname(__file__)

class TrayIcon(QSystemTrayIcon):
  def __init__(self, mainWindow):
    super(TrayIcon, self).__init__()
    self.setIcon(QIcon(os.path.join(basedir, "ui/images/logo32x32.png")))
    trayShowAction = QAction(QIcon(u":/icons/images/eye.svg"), "Открыть", self)
    trayQuitAction = QAction(QIcon(u":/icons/images/log-out.svg"), "Выйти", self)

    trayShowAction.triggered.connect(lambda: mainWindow.show())
    trayQuitAction.triggered.connect(lambda: utils.quit())

    self.messageClicked.connect(lambda: mainWindow.show())
    self.activated.connect(lambda reason: mainWindow.show() if QSystemTrayIcon.ActivationReason.Trigger == reason else None)

    self.menu = QMenu()
    self.menu.setStyleSheet('color: #f5f5f5; font-family: Rubik; background-color: #13171c;')
    self.menu.addAction("ArciBinder").setEnabled(False)
    self.menu.addSeparator()
    self.menu.addAction(trayShowAction)
    self.menu.addAction(trayQuitAction)

    self.setContextMenu(self.menu)
    self.show()