# 10 - Mar - 2020

# Two-Sum

# You are given a list of numbers, and a target number k.
# Return whether or not there are two numbers in the list that add up to k.
#
# Example:
# Given [4, 7, 1 , -3, 2] and k = 5,
# return true since 4 + 1 = 5.

def two_sum(list, k):
    # Fill this in.
    for i in range(len(list)):
        num = k - list[i]
        if num in list[i+1:]:
            return True
        exit()
    return False

print two_sum([4,7,1,-3,2], 5)
print two_sum([10, 5, 3, 7, 3], 6)
# True
