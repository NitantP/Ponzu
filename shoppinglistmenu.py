import json
import ShoppingList
import sys

def shoppinglist_menu():
    print("Welcome to your shopping list!")

    try:
        with open("shoppinglist.json") as myShoppingList:
            shoppinglist = ShoppingList.ShoppingList(json.load(myShoppingList))
        print("-- Found an existing file!\n")
    except:
        shoppinglist = ShoppingList.ShoppingList()
        print("-- No existing file found. Here's a fresh shopping list!\n")

    while True:
        print("[0] Print current shopping list")
        print("[1] Add item to shopping list")
        print("[2] Delete shopping list")
        print("[3] Save shopping list")
        print("[q] Exit")
        
        shoppinglistnav = input("\nChoose an option from above: ")
        print("===========================================")

        if shoppinglistnav == '0':
            shoppinglist.toString()
        elif shoppinglistnav == '1':
            print(shoppinglist.add_item(input("Name: ")))
        elif shoppinglistnav == '2':
            print(shoppinglist.delete(input("Name: ")))
        elif shoppinglistnav == '3':
            print(shoppinglist.save())
        elif shoppinglistnav == 'q':
            shoppinglist.save()
            sys.exit()
        else: 
            print("Invalid choice")
    
        print("===========================================")

if __name__ == "__main__":
    shoppinglist_menu()
