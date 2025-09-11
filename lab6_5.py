"""
    5. Write a program to check if a number harshad's number or not
"""

def isHarshadNumber(n : int) -> bool:
    temp = n
    count = len(str(n))
    return ((n%count) == 0)

n = int(input("Enter Number: "))

if (isHarshadNumber(n)):
    print("Harshad Number")
else:
    print("Not Harshad Number: ")