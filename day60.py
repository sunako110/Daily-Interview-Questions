# 08 - May - 2020

# Reverse Integer

# Write a function that reverses the digits a 32-bit signed integer, x.
# Assume that the environment can only store integers within the 32-bit signed integer range, [-2^31, 2^31 - 1].
# The function returns 0 when the reversed integer overflows.
#
# Example:
# Input: 123
# Output: 321

class Solution:
    def reverse(self, x):
        # Fill this in.
        if not -2**31 <= x <= 2**31 -1:
            return 0
        else:
            num = 0
            i = 0
            for n in str(x):
                num += int(n) * (10 ** i)
                i += 1
            return num

print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
