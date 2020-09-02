# 28 - Apr - 2020

# Reverse Words in a String

# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "The cat in the hat"
# Output: "ehT tac ni eht tah"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

class Solution:
    def reverseWords(self, str):
        # Fill this in.
        str = str[::-1]
        list = str.split()
        list = list[::-1]
        return ' '.join(list)


print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah