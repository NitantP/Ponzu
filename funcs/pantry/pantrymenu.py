print("Welcome to the pantry!\n")

print("[0] Print current pantry\n")
print("[1] Add item to pantry\n")
print("[2] Update item in pantry\n")
print("[3] Delete item from pantry\n")

pantrynav = input("Choose an option (number) from above: ")

if pantrynav == '0':
    print("Printing pantry")
elif pantrynav == '1':
    print("Enter info")
elif pantrynav == '2':
    print("Enter name, info")
elif pantrynav == '3':
    print("Enter name")
else:
    print("Try again")
