"""
    4. Write a program to generate fibonacci series using recursion
"""
def fib(n : int) -> None:
    if (n == 1):
        return 0
    if (n == 2):
        return 1
    return fib(n-1) + fib(n-2)

n = int(input("How many entries: "))

for i in range(1, n+1):
    print(fib(i))