"""
    3. WAP to remove duplicates from a list while preserving order
"""
lst = [3, 1, 2, 3, 4, 2, 5, 1]
unique_list = []
seen = set()
for item in lst:
    if item not in seen:
        unique_list.append(item)
        seen.add(item)
print(unique_list)