"""
    6. Given [(1, 4), (2, 1), (3, 3)], WAP to sort the tuple list by the second element
"""
tuple_list = [(1, 4), (2, 1), (3, 3)]
sorted_list = sorted(tuple_list, key=lambda x:x[1])
print(sorted_list)