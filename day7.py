# 09 - Mar - 2020

# Sorting a list with 3 unique numbers

# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

# Example :
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]

def sortNums(nums):
    # Fill this in.
    quick_sort(nums,0,len(nums)-1)
    return nums

def quick_sort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

def partition (arr,l,h):
    i = l-1
    pivot = arr[h]

    for j in range(l,h):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return (i+1)

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]