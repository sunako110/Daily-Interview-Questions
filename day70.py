# 18 - May - 2020

# Find the Single Element in an Array of Duplicates

# Given an array of integers, arr,
# where all numbers occur twice except one number which occurs once, find the number.
# Your solution should ideally be O(n) time and use constant extra space.
# Example:
# Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
# Output: 7

class Solution(object):
    def findSingle(self, nums):
        # Fill this in.
        nums.sort()
        if len(nums) == 0:
            return
        if len(nums) == 1 or nums[0] != nums[1]:
            return nums[0]
        for i in range(1,len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
        if nums[-1] != nums[-2]:
            return nums[-1]

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3