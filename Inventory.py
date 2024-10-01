'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
'''

import csv

class Inventory:
    location: str
    quantity: int
    price: float
# initializing class attributes
    def __init__(self, location='N/A', quantity=0, price=0.0):
        self.quantity = quantity
        self.price = price
        self.location = 'N/A'

# Creating get and set functions
    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price

    def getLocation(self):
        return self.location

    def setQuantity(self, quantity):
        self.quantity = quantity

    def setPrice(self, price):
        self.price = price

    def setLocation(self, location):
        self.location = location

if __name__ == '__main__':
    inventory = Inventory()
    inventory.setQuantity(10)
    inventory.setPrice(24.45)
    inventory.setLocation("Store # 39")
    print(inventory.getLocation())
    print(inventory.getQuantity())
    print(inventory.getPrice())
