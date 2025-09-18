# Implementation of selection sort
def selectionSort(nums: list[int]) -> list[int]:
    for i in range(0, len(nums)):
        min = i
        for j in range(i, len(nums)):
            if (nums[j] < nums[min]):
                min = j
        
        nums[min], nums[i] = nums[i], nums[min]
    
    return nums
nums = [5, 2, 8, 1, 9, 4, 6, 3, 7]
print(f"Sorted Array: {selectionSort(nums)}")