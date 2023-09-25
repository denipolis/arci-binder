import keyboard
import time
import os
import winreg as reg
import sys
from ctypes import windll
import win32gui

def singleKeyPress(key: str) -> None:
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)
    time.sleep(0.1)

def quit() -> None:
    os._exit(0)

def isAppFullScreen():
    user32 = windll.user32
    user32.SetProcessDPIAware()

    try:
        hWnd = user32.GetForegroundWindow()
        rect = win32gui.GetWindowRect(hWnd)
        return rect == (0, 0, windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1))
    except:
        return False

def openURL(link: str) -> None:
    os.system(f"start \"\" {link}")

def enableAutoRun() -> None:
    currentAppPath = sys.argv[0]

    key = reg.OpenKey(reg.HKEY_CURRENT_USER, 'Software\Microsoft\Windows\CurrentVersion\Run', 0, reg.KEY_SET_VALUE)
    reg.SetValueEx(key, "ArciBinder", 0, reg.REG_SZ, currentAppPath)
    key.Close()

def disableAutoRun() -> None:
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, 'Software\Microsoft\Windows\CurrentVersion\Run', 0, reg.KEY_WRITE)
    reg.DeleteValue(key, "ArciBinder")
    key.Close()

def isAutoRun() -> bool:
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, 'Software\Microsoft\Windows\CurrentVersion\Run', 0, reg.KEY_QUERY_VALUE)
    
    try:
        reg.QueryValueEx(key, "ArciBinder")
        return True
    except:
        return False