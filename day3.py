# 05 - Mar - 2020

# Longest Palindromic Substring

# A palindrome is a sequence of characters that reads the same backwards and forwards.
# Given a string, s, find the longest palindromic substring in s.

# Example:
# Input: "banana"
# Output: "anana"

# Input: "million"
# Output: "illi"

class Solution:
    def longestPalindrome(self, s):
        # Fill this in.
        start_pos = (len(s)-1)/2
        end_pos = -((len(s)-1)/2 + 1)
        while start_pos > 0 or end_pos < 0:
            print start_pos, end_pos
            if s[start_pos] == s[end_pos + 1] and end_pos + 1 < 0:
                end_pos += 1
            elif s[start_pos - 1] == s[end_pos] and start_pos - 1 >= 0:
                start_pos -=1
            else:
                if s[start_pos - 1] == s[end_pos + 1] and end_pos + 1 < 0 <= start_pos - 1:
                    start_pos -= 1
                    end_pos += 1
                else:
                    break
        return s[start_pos:end_pos + 1] if end_pos != -1 else s[start_pos:]


# Test program
s = "tracecars"
print(s[-1])
print(str(Solution().longestPalindrome(s)))
# racecar