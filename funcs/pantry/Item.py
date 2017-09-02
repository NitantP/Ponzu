class Item:
    
    def __init__(self, name, purchase_date, expiration_date, quantity):
        self.name = name
        self.purchase_date = purchase_date
        self.expiration_date = expiration_date
        self.quantity = quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_pdate(self, pdate):
        self.purchase_date = pdate

    def set_edate(self, edate):
        self.expiration_date = edate

    def get_quantity(self):
        return self.quantity

    def get_pdate(self):
        return self.purchase_date

    def get_edate(self):
        return self.expiration_date


