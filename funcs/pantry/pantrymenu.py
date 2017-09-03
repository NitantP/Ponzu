import Pantry
import dill
import sys

try:
    with open("pantry.txt", "rb") as myPantry:
        pantry = dill.loads(myPantry)
except:
    pantry = Pantry.Pantry()

print("Welcome to the pantry!\n")

pantrynav = -1

while int(pantrynav) < 4:
    print("[0] Print current pantry\n")
    print("[1] Add item to pantry\n")
    print("[2] Update item in pantry\n")
    print("[3] Delete item from pantry\n")

    pantrynav = input("Choose an option (number) from above: ")

    if pantrynav == '0':
        pantry.peek()
    elif pantrynav == '1':
        iname = input("Name: ")
        ipdate = input("Purchase date: ")
        iedate = input("Expiration date: ")
        iquantity = input("Quantity: ")
        print("\n")
        pantry.add_item(iname, ipdate, iedate, iquantity)
    elif pantrynav == '2':
        print("Enter name, info")
    elif pantrynav == '3':
        pantry.save()
        sys.exit()
    else:
        print("Try again")
