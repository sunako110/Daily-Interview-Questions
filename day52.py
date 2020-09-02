# 30 - Apr - 2020

# Product of Array Except Self

# You are given an array of integers.
# Return an array of the same size where the element at each index is the product of
# all the elements in the original array except for the element at that index.
#
# For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].
#
# You cannot use division in this problem.

def products(nums):
    # Fill this in.
    ans = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        ans.append(product)
    return ans



print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]