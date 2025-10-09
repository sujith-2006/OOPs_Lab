# Write program to demonstrate non parametric constructor

class Book:
    def __init__(self):
        self.name = "Harry Potter"
        self.price = 45
        self.pages = 366
    
    def display(self):
        print(f"Name: {self.name}\nPrice: ${self.price}\nPages: {self.pages}")
        return

b = Book()
b.display()