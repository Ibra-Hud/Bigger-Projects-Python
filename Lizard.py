'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
'''

import Reptile as R
import csv

class Lizard(R.Reptile):
    habitat: str
    frill: bool
    spikes: bool

    # initializing class variables
    def __init__(self, name = 'Snake',  size ='S', weight = 1.0):
        R.Reptile.__init__(self)
        self.habitat = "Arid"
        self.frill = False
        self.spikes = False
        self.TYPE = "Lizard"
        self.setName(name)
        self.size = size
        self.weight = weight
# creating set and get functions
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

    def getHabitat(self):
        return self.habitat
    def setHabitat(self, habitat):
        self.habitat = habitat

    def hasFrill(self):
        return self.frill
    def setFrill(self, frill):
        self.frill = frill

    def hasSpikes(self):
        return self.spikes
    def setSpikes(self, spikes):
        self.spikes = spikes

if __name__ == "__main__":
    lizard = Lizard()
    lizard.setFrill(True)
    lizard.setHabitat("Forest")
    lizard.setSpikes(False)
    print('Type', lizard.TYPE)
    print("Frill",lizard.hasFrill())
    print("Spikes",lizard.hasSpikes())
    print("Habitat", lizard.getHabitat())
    lizard.inventory.setLocation("Store #14")
    lizard.inventory.setQuantity(20)
    lizard.inventory.setPrice(12.20)

    print('ColdBlooded', lizard.isColdBlooded())
    print('Food', lizard.getFood())
    print('animal')
    print('MultiCellular', lizard.isMultiCellular())
    print('SexualReproduction', lizard.hasSexualReproduction())
    print('Heterotroph', lizard.isHeterotroph())
    print('Inventory')
    print('Location', lizard.inventory.getLocation())
    print('Quantity', lizard.inventory.getQuantity())
    print('Price', lizard.inventory.getPrice())
