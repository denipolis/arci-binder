import os

windowNames = ['mainWindow', 'profileDeleteWindow', 'profileEditWindow', 'profileListWindow']

for name in windowNames:
    os.system(f"{os.getcwd()}\\env\\Scripts\\pyuic6.exe -x src/ui/{name}.ui -o src/{name}.py")
    print(f"\033[92m{name} - OK!")

print("\033[0m")