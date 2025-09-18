# Implementation of Linear and Binary search

def linearSearch(arr: list[int], target: int) -> int:
    for i in range(0, len(arr)):
        if (arr[i] == target):
            return i
    
    return -1
def binarySearch(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    
    while (left <= right):
        mid = (left + right) // 2
        if (arr[mid] == target):
            return mid
        elif(arr[mid] > target):
            right = mid - 1
        else:
            left = mid + 1
            
nums = [2, 5, 8, 10, 15, 18, 22, 45]
print(f"Item at position: {linearSearch(nums, 45) + 1}")
print(f"Item at position: {binarySearch(nums, 8) + 1}")
