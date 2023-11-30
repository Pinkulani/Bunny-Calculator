# @Pinkulani 30.11.2023

from Modules.Arithmetic import *
from Modules.Pythagoras import *

print("|- Bunny Calculator -| \n")
print("Modules included:")

Modules = ["Arithmetic", "Pythagoras"]
for X in range(0, len(Modules)):
    print("- ", Modules[X])

print("")
while True:
    Mode = int(input("Choose type: "))
    match Mode:
        case 1:
            Arithmetic()
            break
        case 2:
            Pythagoras()
            break
        case _:
            print("Invalid input!")
            continue
