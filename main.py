import pantrymenu
import sys

print("\nWelcome to Ponzu!")

menunav = 0

while True:
        print("[0] Pantry")
        print("[1] Budget")
        print("[q] Quit")
        
        menunav = input("\nChoose an option from above: ")
        print("===========================================")

        if menunav == '0':
            pantrymenu.pantry_menu()
        elif menunav == '1':
            print("Budgeting coming soon!")
        elif menunav == 'q':
            sys.exit()
        else:
            print("Invalid choice")

        print("===========================================")

