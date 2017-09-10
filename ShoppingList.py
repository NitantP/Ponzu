import json
import bisect

class ShoppingList:

    def __init__(self, shoppinglist=None):
        if shoppinglist is None:
            self.shoppinglist = []
        else:
            self.shoppinglist = shoppinglist
        self.size = 0

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
            return "[" + iname + "] -- added"

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
