import json
import Item

class Pantry:

    def __init__(self, pantry=None):
        if pantry is None:
            self.pantry = {}
        else:
            self.pantry = pantry
        
        self.size = 0
    
    def toString(self):
        print("Size of pantry: " + str(self.size) + "\n")
        for iname, attr in self.pantry.items():
            print(iname + "\t" + attr[0] + " " + attr[1] + " " + attr[2] + "\n")

    def add_item(self, name, purchase_date, expiration_date, quantity):
        self.pantry[name] = [purchase_date, expiration_date, quantity]
        self.size += 1
    
    def save(self):
        with open("pantry.json", "w") as myPantry:
            json.dump(self.pantry, myPantry, indent=4, sort_keys=True)
