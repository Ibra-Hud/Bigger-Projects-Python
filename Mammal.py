'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
'''

import Animal as A
import csv

class Mammal(A.Animal):
    warmBlooded: bool
    fur: bool
# initializing class variables
    def __init__(self):
        A.Animal.__init__(self)
        self.fur = True
        self.warmBlooded = True
        self.TYPE = 'Mammal'

    # Creating set and get functions for the class
    def isWarmBlooded(self):
        return self.warmBlooded

    def setWarmBlooded(self, warmBlood):
        self.warmBlooded = bool(warmBlood)

    def hasFur(self):
        return self.fur

    def setFur(self, fur):
        self.fur = bool(fur)

if __name__ == "__main__":
    mammal = Mammal()
    mammal.inventory.setLocation("Store #14")
    mammal.inventory.setQuantity(20)
    mammal.inventory.setPrice(12.20)
    print("Type : ", mammal.TYPE)
    print('WarmBlooded', mammal.isWarmBlooded())
    print('Fur', mammal.hasFur())
    print('animal')
    print('MultiCellular', mammal.isMultiCellular())
    print('SexualReproduction', mammal.hasSexualReproduction())
    print('Heterotroph', mammal.isHeterotroph())
    print('Inventory')
    print('Location', mammal.inventory.getLocation())
    print('Quantity', mammal.inventory.getQuantity())
    print('Price', mammal.inventory.getPrice())
