"""
    4. WAP to rotate a list to the left / right by k positions using slicing and loop
"""

lst = [1, 2, 3, 4, 5]
k = 2 
n = len(lst)
k = k % n

#Left rotation
rotated_left = lst[k:] + lst[:k]

#Right rotation
rotated_right = lst[-k:] + lst[:-k]

print(rotated_left)
print(rotated_right)