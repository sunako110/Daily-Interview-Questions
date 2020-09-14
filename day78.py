# 27 - May - 2020

# Subarray With Target Sum

# You are given an array of integers, and an integer K.
# Return the subarray which sums to K. You can assume that a solution will always exist.

def find_continuous_k(list, k):
    sum = 0
    if not list:
        return
    for i in range(len(list)):
        sum += list[i]
        if sum == k:
            return list[0:i+1]
        if sum > k:
            return find_continuous_k(list[1:],k)


print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]