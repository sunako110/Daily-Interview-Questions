# 06 - Apr - 2020

# Contiguous Subarray with Maximum Sum

# You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.
#
# Example:
#
# [34, -50, 42, 14, -5, 86]
#
# Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].
#
# Your solution should run in linear time.
import sys

def max_subarray_sum(arr):
  # Fill this in.
    sum = [0]
    min = sys.maxsize
    max = - sys.maxsize
    start = 0
    end = len(arr)
    for i in range(len(arr)):
        sum.append(arr[i]+sum[i])
        if arr[i]+sum[i] >= max:
            end = i + 1
            max = arr[i]+sum[i]
        if arr[i]+sum[i] <= min:
            start = i + 1
            min = arr[i]+sum[i]

    return "The maximum sum is " + str(max - min) + " for the contiguous subarray " + str(arr[start:end])

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
