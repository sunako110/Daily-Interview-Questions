# 17 - Mar - 2020

# Find Pythagorean Triplets

# Given a list of numbers, find if there exists a pythagorean triplet in that list.
# A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2

# Example:
# Input: [3, 5, 12, 5, 13]
# Output: True
# Here, 52 + 122 = 132.

import math

def findPythagoreanTriplets(nums):
    # Fill this in.
    maximum = 0
    for i in range(len(nums)):
        maximum = max(maximum,nums[i])

    hash = [0] * (max(nums)+1)

    for i in range(len(nums)):
        hash[nums[i]] += 1

    for i in range(1, maximum+1):
        if hash[i] == 0:
            continue

        for j in range(1, maximum+1):
            if (i == j and hash[i] == 1) or hash[j] == 0:
                continue

            val = int(math.sqrt(i * i + j * j))

            if val * val != i * i + j * j:
                continue

            if val > maximum:
                continue

            if hash[val]:
                return True

    return False

print(findPythagoreanTriplets([3, 12, 5, 13]))
# True