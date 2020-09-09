# 20 - May - 2020

# String Compression

# Given an array of characters with repeats, compress it in place.
# The length after compression should be less than or equal to the original array.
#
# Example:
# Input: ['a', 'a', 'b', 'c', 'c', 'c']
# Output: ['a', '2', 'b', 'c', '3']

class Solution(object):
    def compress(self, chars):
        # Fill this in.
        chars.sort()
        result = []
        repeat = 1
        for i in range(len(chars)-1):
            if chars[i] == chars[i+1]:
                repeat += 1
            elif repeat > 1:
                result.append(chars[i])
                result.append(repeat)
                repeat = 1
            else:
                result.append(chars[i])
        if repeat > 1:
            result.append(chars[-1])
            result.append(repeat)
        else:
            result.append(chars[-1])
        return result

print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']