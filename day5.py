# 07 - Mar - 2020

# First and Last Indices of an Element in a Sorted Array

# Given a sorted array, A, with possibly duplicated elements,
# find the indices of the first and last occurrences of a target element, x.
# Return -1 if the target is not found.

# Example:
# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]
#
# Input: A = [100, 150, 150, 153], target = 150
# Output: [1,2]
#
# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]

class Solution:
    def getRange(self, arr, target):
        # Fill this in.
        # first = arr.index(target)
        # if first == -1:
        #     last = -1
        # else:
        #     last = first
        #     for i in range(first + 1,len(arr)):
        #         if arr[i] == target:
        #             last = i
        # return [first,last]
        index = [i for i,x in enumerate(arr) if x == target]
        if len(index) > 0:
            return [index[0],index[-1]] if len(index) > 1 else [index[0],index[0]]
        else:
            return [-1,-1]

# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]