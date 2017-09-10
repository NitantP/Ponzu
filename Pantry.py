import json


class Pantry:

    def __init__(self, pantry=None):
        if pantry is None:
            self.pantry = {}
            self.size = 0
        else:
            self.pantry = pantry
            self.size = len(pantry)
    
    def toString(self):
        """Used to print contents of the pantry."""
        print("Size of pantry: " + str(self.size) + "\n")
        for iname, attr in self.pantry.items():
            print(iname + "\t" + attr[0] + " " + attr[1] + " " + attr[2])

    def add_item(self, name, purchase_date, expiration_date, quantity):
        if name in self.pantry:
            return "\nItem is already in the pantry. Try updating it instead!"
        else:
            self.pantry[name] = [purchase_date, expiration_date, quantity]
            self.size += 1
            return "\n" + name + ": [" + purchase_date + ", " \
                    + expiration_date + ", " + quantity + "] -- added"
    
    def save(self):
        with open("pantry.json", "w") as myPantry:
            json.dump(self.pantry, myPantry, indent=4, sort_keys=True)
        return "Pantry saved!"
    
    def search(self, iname):
        attr = self.pantry[iname]
        return iname + " " + attr[0] + " " + attr[1] + " " + attr[2]

    def update(self, new_list):
        old_attr = self.pantry[new_list[0]]
        
        if new_list[1] == "purchase date":
            old_attr[0] = new_list[2]
        elif new_list[1] == "expiration date":
            old_attr[1] = new_list[2]
        elif new_list[1] == "quantity":
            old_attr[2] = new_list[2]
        else:
            return "Update failed: invalid attribute"
        
        self.pantry[new_list[0]] = old_attr

        return "Update completed (" + new_list[1] + " --> " + new_list[2] + ")"
