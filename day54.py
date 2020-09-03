# 02 - May - 2020

# Longest Increasing Subsequence

# You are given an array of integers.
# Return the length of the longest increasing subsequence (not necessarily contiguous) in the array.
#
# Example:
# [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
#
# The following input should return 6 since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.
import sys

def subsequence(list):
# recursive method:

#     return length(list, -sys.maxsize, 0)
#
# def length(list, prev, cur):
#     if (cur == len(list)):
#         return 0
#     taken = 0
#     if (list[cur] > prev):
#         taken = 1 + length(list, list[cur], cur + 1)
#     not_taken = length(list, prev, cur + 1)
#     return max(taken, not_taken)

# dynamic programming:
    if len(list) == 0:
        return 0
    dp = [1] * len(list)
    for i in range(1, len(list)):
        maxval = 0
        for j in range(0,i):
            if list[i] > list[j]:
                maxval = max(maxval,dp[j])
        dp[i] = maxval + 1
    return max(dp)

list = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(subsequence(list))