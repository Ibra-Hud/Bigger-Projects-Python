import AggieBook as AB

'''
    Test 1-5 will test the default settings of the constructor
'''
# test 1
print("Test 1")
book = AB.AggieBook("Intro to Python", "March 12 2023", 3, 76.34)
print(book)
print("\n")

# test 2
print("Test 2")
book = AB.AggieBook("Intro to Python", "March 12 2023", 3)
print(book)
print("\n")

# test 3
print("Test 3")
book = AB.AggieBook("Intro to Python", "March 12 2023")
print(book)
print("\n")

# test 4
print("Test 4")
book = AB.AggieBook("Intro to Python")
print(book)
print("\n")

# test 5
print("Test 5")
book = AB.AggieBook()
print(book)
print("\n")

'''
    Test 6 - 10 will test the mutator for category getter and setter
'''
# test 6
print("Test 6")
book = AB.AggieBook("Intro to Python", "March 12 2023", 1, 76.34)
print(book)
print("\n")

print("Test 7")
book = AB.AggieBook("Intro to Python", "March 12 2023", 2, 76.34)
print(book)
print("\n")

print("Test 8")
book = AB.AggieBook("Intro to Python", "March 12 2023", 3, 76.34)
print(book)
print("\n")

print("Test 9")
book = AB.AggieBook("Intro to Python", "March 12 2023", 5, 76.34)
print(book)
print("\n")

print("Test 10")
book = AB.AggieBook("Intro to Python", "March 12 2023", 0, 76.34)
print(book)
print("\n")
'''
    Test 11 - 13 will test the Class Vars
'''
print("Test 11")
print(str(AB.AggieBook.stateTax))
print("\n")

print("Test 12")
print(str(AB.AggieBook.fedTax))
print("\n")

print("Test 13")
print(str(AB.AggieBook.aggieCategories))
print("\n")

'''
    Test 14 - 16 will test the setBook method
'''
print("Test 14")
book = AB.AggieBook()
print(str(book.sellBook(0)))
print("\n")

print("Test 15")
book = AB.AggieBook()
book.setPrice(10.5)
print(str(book.sellBook(1)))
print("\n")

print("Test 16")
book = AB.AggieBook()
book.setPrice(10.5)
print(str(book.sellBook(100)))
