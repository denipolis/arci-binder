@echo off

mkdir build\workcache
mkdir build\runcache
mkdir build\dist

rem call "tools\translateUI.bat"
rem call "env\Scripts\pyinstaller.exe" --log-level DEBUG --noconfirm main.spec
call "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss 

rem rd /s /q dist
rem rd /s /q build\main
rem rd /s /q build\workcache
rem rd /s /q build\runcache
rem rd /s /q build\dist