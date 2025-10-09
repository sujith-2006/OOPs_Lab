# Write program to demonstrate parametrized constructor

class Book:
    def __init__(self, name, price, pages):
        self.name = name
        self.price = price
        self.pages = pages
    
    def display(self):
        print(f"Name: {self.name}\nPrice: ${self.price}\nPages: {self.pages}")
        return
    
b = Book("Harry Potter", 35, 90)
b.display()