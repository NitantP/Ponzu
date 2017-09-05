import Pantry
import json
import sys

print("Welcome to the pantry")

try:
    with open("pantry.json", "r") as myPantry:
        pantry = Pantry.Pantry(json.load(myPantry))
        print("-- Found an existing file!\n")
except:
    pantry = Pantry.Pantry()
    print("-- No existing file found, here's a fresh pantry!\n")

pantrynav = -1

while int(pantrynav) < 3:
    print("[0] Print current pantry\n")
    print("[1] Add item to pantry\n")
    print("[2] Save pantry\n")

    pantrynav = input("Choose an option (number) from above: ")
    print("===========================================")

    if pantrynav == '0':
        pantry.toString()
    elif pantrynav == '1':
        iname = input("Name: ")
        ipdate = input("Purchase date: ")
        iedate = input("Expiration date: ")
        iquantity = input("Quantity: ")
        pantry.add_item(iname, ipdate, iedate, iquantity)
    elif pantrynav == '2':
        pantry.save()
        sys.exit()
    else:
        print("Try again")

    print("===========================================")
