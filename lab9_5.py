# Write program to demonstrate constructor overloading

class Student:
    
    def __init__(self, name):
        self.name = name
        
    def __init__(self, name, age):
        self.name = name
        self.age = age


emma = Student("Emma")
kelly = Student("Kelly", 13)