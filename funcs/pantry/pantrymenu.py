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
    print("-- No existing file found. Here's a fresh pantry!\n")

while True:
    print("[0] Print current pantry\n")
    print("[1] Add item to pantry\n")
    print("[2] Save pantry\n")
    print("[3] Update pantry item\n")
    print("[4] Search pantry for item\n")
    print("[q] Exit pantry system\n")

    pantrynav = input("Choose an option from above: ")
    print("===========================================")

    if pantrynav == '0':
        pantry.toString()
    elif pantrynav == '1':
        iname = input("Name: ")
        ipdate = input("Purchase date: ")
        iedate = input("Expiration date: ")
        iquantity = input("Quantity: ")
        print(pantry.add_item(iname, ipdate, iedate, iquantity))
    elif pantrynav == '2':
        print(pantry.save())
    elif pantrynav == '3':
        new_attr = []
        print("Enter the name of item to update and information to update")
        new_attr.append(input("Name: "))
        new_attr.append(input("Attribute: "))
        new_attr.append(input("Value: "))
        print(pantry.update(new_attr))
    elif pantrynav == '4':
        print(pantry.search(input("Name: ")))
    elif pantrynav == 'q':
        sys.exit()
    else:
        print("Invalid choice")

    print("===========================================")
