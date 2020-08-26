# 11 - Mar - 2020

# Find the non-duplicate number

# Given a list of numbers, where every number shows up twice except for one number, find that one number.

# Example:
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: 1

def singleNumber(nums):
    # Fill this in.
    for i in range(len(nums)):
        min = i
        for j in range(i+1,len(nums)):
            if nums[j] <= nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
    for i in range(len(nums)):
        if i == 0 and nums[i] != nums[i+1]:
            return nums[i]
        if i == len(nums) - 1 and nums[i] != nums[i-1]:
            return nums[i]
        if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
            return nums[i]

print singleNumber([4, 3, 2, 4, 1, 3, 2])
# 1