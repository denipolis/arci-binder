import keyboard
import time
import os
import winreg as reg
import sys
from ctypes import wintypes, windll, create_unicode_buffer

def singleKeyPress(key: str) -> None:
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)
    time.sleep(0.1)

def quit() -> None:
    os._exit(0)

def getActiveWindowTitle() -> str:
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)
    
    if buf.value:
        return buf.value
    else:
        return "NOTHING"

def openURL(link: str) -> None:
    os.system(f"start \"\" {link}")

def enableAutoRun() -> None:
    currentAppPath = sys.argv[0]

    key = reg.OpenKey(reg.HKEY_CURRENT_USER, 'Software\Microsoft\Windows\CurrentVersion\Run', 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(key, "ArciBinder", 0, reg.REG_SZ, currentAppPath)
    key.Close()

def disableAutoRun() -> None:
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, 'Software\Microsoft\Windows\CurrentVersion\Run', 0, reg.KEY_ALL_ACCESS)
    reg.DeleteValue(key, "ArciBinder")
    key.Close()

def isAutoRun() -> bool:
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, 'Software\Microsoft\Windows\CurrentVersion\Run', 0, reg.KEY_ALL_ACCESS)
    
    try:
        reg.QueryValueEx(key, "ArciBinder")
        return True
    except:
        return False