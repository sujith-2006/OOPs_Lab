"""
    1. Write a program to create a function to reverse a number and a string
"""

def reverse(s):
    if (type(s) == str):
        print(s[::-1])
        return 
    elif (type(s) == int):
        temp = s
        new_num = 0
        while (temp != 0):
            new_num = (new_num*10) + (temp%10)
            temp = temp // 10
        print(new_num)
        return 

reverse(1234)
reverse("Hello")