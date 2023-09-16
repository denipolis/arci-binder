@echo off

color 7

mkdir build\workcache
mkdir build\runcache
mkdir build\dist

"env\Scripts\python.exe" tools\compileUI.py
"env\Scripts\pyinstaller.exe" --noconfirm main.spec
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss 

rd /s /q dist
rd /s /q build\main
rd /s /q build\workcache
rd /s /q build\runcache
rd /s /q build\dist