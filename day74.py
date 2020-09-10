# 22 - May - 2020

# Make the Largest Number

# Given a number of integers, combine them so it would create the largest number.
#
# Example:
# Input:  [17, 7, 2, 45, 72]
# Output:  77245217

def largestNum(nums):
    # Fill this in.
    nums = list(map(str, nums))
    nums.sort(reverse=True)
    result = nums[0]
    for i in range(len(nums)-1):
        if int(nums[i] + nums[i+1]) < int(nums[i+1] + nums[i]):
            index = len(result) - len(nums[i])
            result = result[:index] + nums[i+1] + result[index:]
        else:
            result += nums[i+1]
    return result


print(largestNum([17, 7, 2, 45, 72]))
# 77245217