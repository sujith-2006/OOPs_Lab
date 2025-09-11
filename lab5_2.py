"""
    2. Count how many times a substring appears in a string
"""
string = "abababa"
substring = "aba"

count = 0
start = 0

while True:
    start = string.find(substring, start)
    if start == -1:
        break
    count += 1
    start += 1
print(count)