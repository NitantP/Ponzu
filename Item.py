class Item:
    
    def __init__(self, name, purchase_date, expiration_date, quantity):
        self._name = name
        self._purchase_date = purchase_date
        self._expiration_date = expiration_date
        self._quantity = quantity

    def __str__(self):
        return self._name + "\t" + self._purchase_date + "\t" + self._expiration_date + "\t" + self._quantity + "\n"

    #Name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    #Quantity
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @quantity.deleter
    def quantity(self):
        del self._quantity
    
    #Purchase date
    @property
    def purchase_date(self):
        return self._purchase_date
    
    @purchase_date.setter
    def purchase_date(self, value):
        self._purchase_date = value

    @purchase_date.deleter
    def purchase_date(self):
        del self._purchase_date
    
    #Expiration date
    @property
    def expiration_date(self):
        return self._expiration_date
    
    @expiration_date.setter
    def expiration_date(self, value):
        self._expiration_date = value

    @expiration_date.deleter
    def expiration_date(self):
        del self._expiration_date    
