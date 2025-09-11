"""
    3. Write a program to identify all strong numbers in a range from 100 - 1000
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


for i in range(100, 1001):
    if isStrong(i):
        print(i)
    