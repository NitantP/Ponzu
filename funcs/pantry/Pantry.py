import dill
import Item

class Pantry:

    def __init__(self):
        self.pantry = {}
        self.size = 0

    def __str__(self):
        return ''.join('{}'.format(Item) for iname, Item in self.pantry.items())
    
    def add_item(self, name, purchase_date, expiration_date, quantity):
        new_item = Item.Item(name, purchase_date, expiration_date, quantity)
        self.pantry[name] = new_item
        self.size += 1

    def peek(self):
        for iname, Item in self.pantry.items():
            print(Item)
    
    def save(self):
        with open("pantry.txt", "wb") as myPantry:
            dill.dump(self.pantry, myPantry)


