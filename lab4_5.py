"""
    5. find the intersection and union of two lists without using set().
"""

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

intersection = []
for item in list1:
    if item in list2 and item not in intersection:
        intersection.append(item)

union = list1.copy()

for item in list2:
    if item not in union:
        union.append(item)
        
print(intersection)
print(union)
