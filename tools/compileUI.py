import os

windowNames = [name.replace(".ui", "") for name in os.listdir("src/ui") if name.endswith("ui")]
resourceNames = [name.replace(".qrc", "") for name in os.listdir("src/ui") if name.endswith("qrc")]

for resource in resourceNames:
    os.system(f"{os.getcwd()}\\env\\Scripts\\pyside6-rcc.exe src/ui/{resource}.qrc -o src/windows/{resource}_rc.py")
    print(f"\033[92m{resource} - OK!")

for window in windowNames:
    os.system(f"{os.getcwd()}\\env\\Scripts\\pyside6-uic.exe --from-imports src/ui/{window}.ui -o src/windows/{window}.py")
    print(f"\033[92m{window} - OK!")

print("\033[0m")