@echo off

mkdir build\workcache
mkdir build\runcache
mkdir build\dist

call "tools\translateUI.bat"
call "env\Scripts\pyinstaller.exe" --log-level DEBUG --noconfirm main.spec
call "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss 

rd /s /q dist
rd /s /q build\main
rd /s /q build\workcache
rd /s /q build\runcache
rd /s /q build\dist