# @Pinkulani 30.11.2023

from Modules.Arithmetic import *

print("Bunny Calculator")
while True:
    Mode = int(input("Choose type: "))
    match Mode:
        case 1:
            Add()
            break
        case 2:
            print("2")
            break
        case _:
            print("Invalid input")
            continue
