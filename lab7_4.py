# Implementation of Insertion Sort
def insertionSort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while ((j > -1) and (key < nums[j])):
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

nums = [5, 2, 8, 1, 9, 4, 6, 3, 7]
print(f"Sorted Array: {insertionSort(nums)}")