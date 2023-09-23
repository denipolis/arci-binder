import os

print(os.listdir("src/ui/"))

windowNames = [name.replace(".ui", "") for name in os.listdir("src/ui") if name.endswith("ui")]

for name in windowNames:
    os.system(f"{os.getcwd()}\\env\\Scripts\\pyuic6.exe -x src/ui/{name}.ui -o src/windows/{name}.py")
    print(f"\033[92m{name} - OK!")

print("\033[0m")