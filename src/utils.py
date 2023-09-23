import keyboard
import time
import os
from ctypes import wintypes, windll, create_unicode_buffer

def singleKeyPress(key: str):
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)
    time.sleep(0.1)

def quit():
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

def openURL(link: str):
    os.system(f"start \"\" {link}")