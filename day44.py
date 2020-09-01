# 21 - Apr - 2020

# 3 Sum

# Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that a + b + c = 0.
# Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.
#
# Example:
# Input: nums = [0, -1, 2, -3, 1]
# Output: [0, -1, 1], [2, -3, 1]

class Solution(object):
  def threeSum(self, nums):
        # Fill this in.
        answer = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if sum([nums[i],nums[j],nums[k]]) == 0:
                        answer.append([nums[i],nums[j],nums[k]])
        return answer

# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))

# [[-2, 1, 1]]