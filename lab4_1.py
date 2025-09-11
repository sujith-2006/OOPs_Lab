"""
    1. WAP to find the second largest number in a list without using built-in sorting.
"""

nums = [5, 3, 9, 2, 8, 6]
if len(nums) < 2:
    result = None
else:
    largest = second_largest = None
    for num in nums:
        if ((largest is None) or (num > largest)):
            second_largest = largest
            largest = num
        elif((num != largest) and (second_largest is None or num > second_largest)):
            second_largest = num
        result = second_largest

print(second_largest)