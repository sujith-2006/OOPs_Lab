# Implementation of Bubble Sort
def bubbleSort(nums: list[int]):
    for i in range(0, len(nums)):
        for j in range(0, len(nums) - i - 1):
            if (nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums
nums = [5, 2, 8, 1, 9, 4, 6, 3, 7]
print(f"Sorted Array: {bubbleSort(nums)}")