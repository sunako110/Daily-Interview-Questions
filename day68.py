# 16 - May - 2020

# Max and Min with Limited Comparisons

# Given a list of numbers of size n, where n is greater than 3,
# find the maximum and minimum of the list using less than 2 * (n - 1) comparisons.

def find_min_max(nums):
    # Fill this in.
    if len(nums) == 1:
        return nums[0], nums[0]

    if len(nums) == 2:
        if nums[0] >= nums[1]:
            return nums[1], nums[0]
        else:
            return nums[0], nums[1]

    mid = int(len(nums)/2)
    left = find_min_max(nums[:mid])
    right = find_min_max(nums[mid:])

    if left[0] < right[0]:
        minimum = left[0]
    else:
        minimum = right[0]
    if left[1] > right[1]:
        maximum = left[1]
    else:
        maximum = right[1]
    return minimum, maximum

print(find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)