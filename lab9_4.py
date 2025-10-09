# Write program to demonstrate default constructor

class Student:
    def __init__(self, name, age = 12, classroom = 7):
        self.name = name
        self.age = age
        self.classroom = classroom
        
    def show(self):
        print(f"Name: {self.name}\nAge: {self.age}\nClassroom: {self.classroom}")

emma = Student("Emma")
emma.show()