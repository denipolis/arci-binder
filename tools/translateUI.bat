@echo off

rem https://stackoverflow.com/q/138497
rem https://stackoverflow.com/q/2048509

setlocal enabledelayedexpansion

for %%f in (src\ui\*.ui) do (
  set /p val=<%%f
  env\Scripts\pyside6-uic.exe --from-imports %%f -o src/windows/%%~nf.py
  echo Translated: [1m[42m%%f[0m
)

for %%f in (src\ui\*.qrc) do (
  set /p val=<%%f
  env\Scripts\pyside6-rcc.exe %%f -o src/windows/%%~nf_rc.py
  echo Translated: [1m[42m%%f[0m
)