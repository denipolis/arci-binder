@echo off

color 7

mkdir build\cache
mkdir build\cache2
mkdir build\output

"env\Scripts\python.exe" tools\compileUI.py
"env\Scripts\pyinstaller.exe" --noconfirm main.spec
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss 

rmdir -r dist
rmdir -r build\main