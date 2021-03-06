# 30 - Mar - 2020

# Move Zeros

# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
  def moveZeros(self, nums):
        # Fill this in.
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i + 1
                while nums[j] == 0:
                    j += 1
                    if j == len(nums):
                        return nums
                nums[i], nums[j] = nums[j], nums[i]
        return nums


nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]