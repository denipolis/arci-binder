from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu
import os
import utils

basedir = os.path.dirname(__file__)

class TrayIcon(QSystemTrayIcon):
  def __init__(self, mainWindow):
    super(QSystemTrayIcon, self).__init__()
    self.setIcon(QIcon(os.path.join(basedir, "ui/images/logo32x32.png")))
    trayShowAction = QAction("Открыть", icon=QIcon(QIcon(os.path.join(basedir, "ui/images/show.png"))), parent=self)
    trayQuitAction = QAction("Выйти", icon=QIcon(QIcon(os.path.join(basedir, "ui/images/cross.png"))), parent=self)

    trayShowAction.triggered.connect(lambda: mainWindow.show())
    trayQuitAction.triggered.connect(lambda: utils.quit())

    self.messageClicked.connect(lambda: mainWindow.show())
    self.activated.connect(lambda reason: mainWindow.show() if QSystemTrayIcon.ActivationReason.Trigger == reason else None)

    self.menu = QMenu()
    self.menu.addAction("ArciBinder").setEnabled(False)
    self.menu.addSeparator()
    self.menu.addAction(trayShowAction)
    self.menu.addAction(trayQuitAction)

    self.setContextMenu(self.menu)
    self.show()