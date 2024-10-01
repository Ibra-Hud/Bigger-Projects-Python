'''
Name: Ibrahim Hudson
Date: 12/08/2023
Course: Comp163 - Section: 010
'''
import string
def init():
    # Contains Book Categories
    AggieBook.aggieCategories = {
        0: 'Unknown',
        1: 'Biology',
        2: 'Physics',
        3: 'Computer Science'
    }
# Class AggieBook to assign variables & Constructors
class AggieBook:
    # Variables
    stateTax = .07
    fedTax = .1
    aggieCategories = dict()

    # Constructors
    def __init__(self, title = 'TBD', date = 'TBD', category = 0, price = 0.0, description = ''):
        self.title = title
        self.date = date
        self.category = category
        self.price = price
        self.description = description
    # sets and gets variables/constructors
    def setTitle(self,title):
        self.title = title

    def getTitle(self):
        return self.title

    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def setCategory(self, category):
        self.category = category
        if category not in AggieBook.aggieCategories.keys():
            self.category = AggieBook.aggieCategories.keys(0)

    def getCategory(self):
        return AggieBook.aggieCategories.get(self.category)
    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price
    # sellBook to get price for order
    def sellBook(self,quantity):
        totalPrice = (self.price + (self.price * AggieBook.stateTax) + (self.price * AggieBook.fedTax)) * quantity
        return totalPrice

    def __str__(self):
        return f'{self.title} {self.getCategory()} {str(self.price)}'

init()