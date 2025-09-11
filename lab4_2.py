"""
    2. Convert a nested list liek [[1, 2], [3, 4, 5], [6]] into [1, 2, 3, 4, 5, 6]
"""
nested_list = [[1, 2], [3, 4, 5]]
flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)
print(flat_list)
