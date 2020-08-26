# coding=utf-8
# 21 - Mar - 2020

# Minimum Size Subarray Sum

# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead.

# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

class Solution:
  def minSubArrayLen(self, nums, s):
    # Fill this in
    min = 99999
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            if sum(nums[i:j]) == s:
                if len(nums[i:j]) < min:
                    min = len(nums[i:j])

    return min

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2
