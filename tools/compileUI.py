import os

names = ['mainWindow', 'profileDeleteWindow', 'profileEditWindow', 'profileListWindow']

for name in names:
    os.system(f"{os.getcwd()}\\env\\Scripts\\pyuic6.exe -x ui/{name}.ui -o {name}.py")
    print(f"\033[92m{name} - OK!")

print("\033[0m")