import Pantry
import json
import sys

try:
    with open("pantry.json", "r") as myPantry:
        pantry = Pantry.Pantry(json.load(myPantry))
        print("Found a pantry!")
except:
    pantry = Pantry.Pantry()

print("Welcome to the pantry!\n")

pantrynav = -1

while int(pantrynav) < 3:
    print("[0] Print current pantry\n")
    print("[1] Add item to pantry\n")
    print("[2] Save pantry\n")

    pantrynav = input("Choose an option (number) from above: ")

    if pantrynav == '0':
        pantry.toString()
    elif pantrynav == '1':
        iname = input("Name: ")
        ipdate = input("Purchase date: ")
        iedate = input("Expiration date: ")
        iquantity = input("Quantity: ")
        print("\n")
        pantry.add_item(iname, ipdate, iedate, iquantity)
    elif pantrynav == '2':
        pantry.save()
        sys.exit()
    else:
        print("Try again")
