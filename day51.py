# 29 - Apr - 2020

# Merge List Of Number Into Ranges

# Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.
#
# Example:
# Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
# Output: ['0->2', '5->5', '7->11', '15->15']
# Assume that all numbers will be greater than or equal to 0, and each element can repeat.

def findRanges(nums):
    # Fill this in.
    start = 0
    repeat = 0
    ans = []
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            repeat += 1
        if nums[start] + (i - start) - repeat != nums[i]:
            ans.append(str(nums[start]) + '->' + str(nums[i-1]))
            start = i
            repeat = 0
    ans.append(str(nums[start]) + '->' + str(nums[len(nums)-1]))

    return ans

print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']