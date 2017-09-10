import json
import bisect

class ShoppingList:

    def __init__(self, shoppinglist=None):
        if shoppinglist is None:
            self.shoppinglist = []
            self.size = 0
        else:
            self.shoppinglist = shoppinglist
            self.size = len(shoppinglist)

    def toString(self):
        print("Size of shopping list: " + str(self.size) + "\n")
        for iname in self.shoppinglist:
            print(iname)
    
    def add_item(self, iname):
        if iname in self.shoppinglist:
            return "\nItem is already on the shopping list!"
        else:
            bisect.insort(self.shoppinglist, iname)
            self.size += 1
            return "\n[" + iname + "] -- added"

    def save(self):
        with open("shoppinglist.json", "w") as myShoppingList:
            json.dump(self.shoppinglist, myShoppingList)
        return "Shopping list saved!"

    def delete(self, iname):
        try:
            self.shoppinglist.remove(iname)
            self.size -= 1
            return "\n[" + iname + "] -- removed"
        except:
            return "\nDelete failed!"

    def pantry_match(self):
        try:
            with open("pantry.json", "r") as myPantry:
                pantry = json.load(myPantry)
        except:
            return

        pantrylist = list(pantry.keys())
        
        matches = 0
        for iname in self.shoppinglist:
            if iname in pantrylist:
                matches += 1
                print(iname + "-- [" + pantry[iname][0] + ", " + \
                        pantry[iname][1] + ", " + pantry[iname][2] + "]")
        print("\n" + str(matches) + " matches found in pantry")
