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
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read+1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    chars[write] = str(read - anchor + 1)
                    write += 1
                anchor = read + 1
        return chars[:write]

print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']