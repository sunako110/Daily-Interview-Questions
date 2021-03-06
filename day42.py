# 19 - Apr - 2020

# Sort Colors

# Given an array with n objects colored red, white or blue,
# sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library sort function for this problem.
#
# Can you do this in a single pass?

# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

class Solution:
  def sortColors(self, nums):
    # Fill this in.
    count_zero = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.insert(0,0)
            count_zero += 1
        if nums[i] == 1:
            nums.pop(i)
            nums.insert(count_zero,1)
    return nums

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]