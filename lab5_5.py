"""
    5. WAP to modify a tuple by converting into a list, changing values and converting it back
"""
tup = (1, 2, 3, 4)
lst = list(tup)
lst[1] = 20
lst.append(5)
tup_modified = tuple(lst)
print(tup_modified)