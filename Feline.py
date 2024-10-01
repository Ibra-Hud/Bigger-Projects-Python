'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
'''

import Mammal as M
import csv

class Feline(M.Mammal):
    size: str
    weight: float
    color: str

    # initializing class variables
    def __init__(self, name = 'Cat',  size ='S', weight = 1.0):
        M.Mammal.__init__(self)
        self.setName(name)
        self.TYPE = "Feline"
        self.size = size
        self.weight = weight
        self.color = "Gray"
# Creating set and get functions
    def purr(self, count):
        while int(count) > 0:
            print('Meow')
            count -= 1

    def getSize(self):
        return self.size

    def setSize(self, string: str):
        self.size = string

    def getWeight(self):
        return self.weight

    def setWeight(self, weight: float):
        self.weight = weight

    def getColor(self):
        return self.color

    def setColor(self, color: str):
        self.color = color

if __name__ == "__main__":
    feline = Feline("Tabby", "S", 12.3)
    feline.purr(2)
    print("Name",feline.getName())
    print("Type",feline.TYPE)
    print("Size",feline.getSize())
    print("Weight",feline.getWeight())
    print("Color",feline.getColor())

    feline.inventory.setLocation("Store #14")
    feline.inventory.setQuantity(20)
    feline.inventory.setPrice(12.20)

    print('WarmBlooded', feline.isWarmBlooded())
    print('Fur', feline.hasFur())
    print('animal')
    print('MultiCellular', feline.isMultiCellular())
    print('SexualReproduction', feline.hasSexualReproduction())
    print('Heterotroph', feline.isHeterotroph())
    print('Inventory')
    print('Location', feline.inventory.getLocation())
    print('Quantity', feline.inventory.getQuantity())
    print('Price', feline.inventory.getPrice())
