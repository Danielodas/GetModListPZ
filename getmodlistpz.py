import os

# Python script developed by Danielodas
# Only avaliable on Windows

print("Only works on Windows\nPython script developed by Daniel 'Danielodas' Lleó\n12/30/2023")
print("-----------------")

user = os.getlogin()

valid_modes = ["Apocalypse", "Survivor", "Builder", "Sandbox"]

gamemode = input("Enter the gamemode of your game (Apocalypse/Survivor/Builder/Sandbox) : ")

while gamemode not in valid_modes:
    gamemode = input("Invalid gamemode. Please enter a valid gamemode (Apocalypse/Survivor/Builder/Sandbox): ")

loadsfolder = f'C:/Users/{user}/Zomboid/Saves/{gamemode}'

try:
    loads = os.listdir(loadsfolder)
    print(f"{gamemode} loads :")
    loadslist = []
    for load in loads:
        loadslist.append(load)
        print(load)
except FileNotFoundError:
    print("Error: folder not found.")

loadname = input("Enter your load name : ")

while loadname not in loadslist:
    print("That is not an actual load.")
    loadname = input("Enter your load name : ")

pzmodlist = f'C:/Users/{user}/Zomboid/Saves/{gamemode}/{loadname}/mods.txt'

ordinalnum = 1

try:
    with open(pzmodlist, 'r') as txt:
        lines = txt.readlines()
except FileNotFoundError:
    print("Error: file not found.")

print(f"Mod list of the game {loadname} :")

for line in lines:
    if "mod =" in line:
        modifyline = line.replace('mod =', f"Mod {ordinalnum} :").rstrip(',\n')
        print(f"{modifyline}")
        ordinalnum += 1

print("-----------------")
input("Press Enter to exit...")