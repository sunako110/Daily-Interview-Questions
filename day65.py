# 13 - May - 2020

# Jump to the End

# Starting at index 0, for an element n at index i, you are allowed to jump at most n indexes ahead.
# Given a list of numbers, find the minimum number of jumps to reach the end of the list.
#
# Example:
# Input: [3, 2, 5, 1, 1, 9, 3, 4]
# Output: 2
# Explanation:
#
# The minimum number of jumps to get to the end of the list is 2:
# 3 -> 5 -> 4

def jumpToEnd(nums):
    # Fill this in.
    dp = [0] * len(nums)
    for i in range(1,len(nums)):
        min = len(nums)
        for j in range(0,i):
            if i <= j + nums[j] and dp[j] + 1 < min:
                min = dp[j] + 1
        dp[i] = min
    return dp[-1]

print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
# 2
