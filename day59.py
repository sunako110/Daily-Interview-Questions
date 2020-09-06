# 07 - May - 2020

# Min Range Needed to Sort

# Given a list of integers,
# return the bounds of the minimum range that must be sorted so that the whole list would be sorted.
#
# Example:
# Input: [1, 7, 9, 5, 7, 8, 10]
# Output: (1, 5)

# Explanation:
# The numbers between index 1 and 5 are out of order and need to be sorted.

def findRange(nums):
    # Fill this in.
    min = len(nums)
    max = 0
    for i in range(1, len(nums)):
        for j in range(0,i):
            if nums[i] < nums[j]:
                if j <= min:
                    min = j
                if i >= max:
                    max = i
    if min >= max:
        return
    else:
        return (min,max)


print(findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)
