# 23 - May - 2020

# Smallest Number that is not a Sum of a Subset of List

# Given a sorted list of positive numbers,
# find the smallest positive number that cannot be a sum of any subset in the list.
#
# Example:
# Input: [1, 2, 3, 8, 9, 10]
# Output: 7
# Numbers 1 to 6 can all be summed by a subset of the list of numbers, but 7 cannot.

def findSmallest(nums):
    # Fill this in.
    i = 1
    for n in nums:
        if n <= i:
            i = i + n
        else:
            return i

print(findSmallest([1, 2, 3, 8, 9, 10]))
# 7
