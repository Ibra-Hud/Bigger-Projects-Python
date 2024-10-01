'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
'''

import os.path

import Inventory as Inv

class Animal:
    multiCellular: bool
    sexualReproduction: bool
    heterotroph: bool
    fourLimbs: bool
    inventory: Inv.Inventory
    backBone: bool
    type: str
    name: str
# initializing class variables
    def __init__(self):
        self.multiCellular = True
        self.sexualReproduction = True
        self.heterotroph = True
        self.fourLimbs = True
        self.inventory = Inv.Inventory()
        self.backBone = True
        self.TYPE = 'Animal'
        self.name = None
# Creating set and get functions for the class
    def isMultiCellular(self):
        return self.multiCellular

    def hasSexualReproduction(self):
        return self.sexualReproduction

    def isHeterotroph(self):
        return self.heterotroph

    def hasFourLimbs(self):
        return self.fourLimbs

    def setFourLimbs(self, hasFourLimbs):
        self.fourLimbs = hasFourLimbs

    def hasBackBone(self):
        return self.backBone

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

if __name__ == '__main__':

    animal = Animal()
    print('type', animal.TYPE)
    print('MultiCellular', animal.isMultiCellular())
    print('SexualReproduction', animal.hasSexualReproduction())
    print('Heterotroph', animal.isHeterotroph())
    print('Inventory')
    print('Location', animal.inventory.getLocation())
    print('Quantity', animal.inventory.getQuantity())
    print('Price', animal.inventory.getPrice())