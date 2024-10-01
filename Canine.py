'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
'''

import Mammal as M
import csv

class Canine(M.Mammal):
    size: str
    weight: float
    color: str

    # initializing class variables
    def __init__(self, name='Dog', size="S", weight=1.0):
        M.Mammal.__init__(self)
        self.setName(name)
        self.TYPE = "Canine"
        self.size = size
        self.weight = weight
        self.color = "Gray"
# Creating set and get functions
    def bark(self, count):
        while int(count) > 0:
            print('Woof')
            count -= 1

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

if __name__ == '__main__':
    canine = Canine("Begle", "M", 12.3)
    canine.bark(3)
    print("Name",canine.getName())
    print("Type",canine.TYPE)
    print("Size",canine.getSize())
    print("Weight",canine.getWeight())
    print("Color",canine.getColor())

    canine.inventory.setLocation("Store #14")
    canine.inventory.setQuantity(20)
    canine.inventory.setPrice(12.20)
    print("Type",canine.TYPE)
    print('WarmBlooded', canine.isWarmBlooded())
    print('Fur', canine.hasFur())
    print('animal')
    print('MultiCellular', canine.isMultiCellular())
    print('SexualReproduction', canine.hasSexualReproduction())
    print('Heterotroph', canine.isHeterotroph())
    print('Inventory')
    print('Location', canine.inventory.getLocation())
    print('Quantity', canine.inventory.getQuantity())
    print('Price', canine.inventory.getPrice())

