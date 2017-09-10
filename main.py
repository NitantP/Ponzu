import pantrymenu
import shoppinglistmenu
import sys

def main_menu():
    print("\nWelcome to Ponzu!")

    while True:
        print("[0] Pantry")
        print("[1] Shopping list")
        print("[q] Quit")
        
        menunav = input("\nChoose an option from above: ")
        print("===========================================")

        if menunav == '0':
            pantrymenu.pantry_menu()
        elif menunav == '1':
            shoppinglistmenu.shoppinglist_menu()
        elif menunav == 'q':
            sys.exit()
        else:
            print("Invalid choice")

        print("===========================================")

if __name__ == "__main__":
    main_menu()

