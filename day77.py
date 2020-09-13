# 25 - May - 2020

# Permutations of numbers

# You are given an array of integers. Return all the permutations of this array.

def permute(nums):
    # Fill this in.
    if not nums:
        return []
    if len(nums) == 1:
        return [nums]
    ans = []
    for i in range(len(nums)):
        n = nums[i]
        for p in permute(nums[:i] + nums[i+1:]):
            ans.append([n] + p)
    return ans


print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]