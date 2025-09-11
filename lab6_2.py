"""
    2. Write a program to check if a number is strong number or not
"""

def fact(n:int) -> int:
    temp = 1
    for i in range(n, 0, -1):
        temp *= i
    return temp

def isStrong(n : int) -> bool:
    
    sum = 0
    temp = n
    while (temp != 0):
        sum += fact(temp%10)
        temp = temp // 10
    
    return (sum == n)

n = int(input("Enter Number: "))

if (isStrong(n)):
    print("Strong Number")
else:
    print("Not Strong Number")
