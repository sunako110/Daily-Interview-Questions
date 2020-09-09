# 19 - May - 2020

# Convert Roman Numerals to Decimal

# Given a Roman numeral, find the corresponding decimal value. Inputs will be between 1 and 3999.
#
# Example:
# Input: IX
# Output: 9
#
# Input: VII
# Output: 7
#
# Input: MCMIV
# Output: 1904

# Roman numerals are based on the following symbols:
# I     1
# IV    4
# V     5
# IX    9
# X     10
# XL    40
# L     50
# XC    90
# C     100
# CD    400
# D     500
# CM    900
# M     1000

# Numbers are strings of these symbols in descending order.
# In some cases, subtractive notation is used to avoid repeated characters. The rules are as follows:
# 1.) I placed before V or X is one less, so 4 = IV (one less than 5), and 9 is IX (one less than 10)
# 2.) X placed before L or C indicates ten less, so 40 is XL (10 less than 50) and 90 is XC (10 less than 100).
# 3.) C placed before D or M indicates 100 less, so 400 is CD (100 less than 500), and 900 is CM (100 less than 1000).

class Solution():
    def romanToInt(self, s):
        # Fill this in.
        if len(s) == 0:
            return
        i = 0
        sum = 0
        while i < len(s):
            if s[i] == 'I':
                if i == len(s) - 1:
                    sum += 1
                elif s[i+1] == 'V':
                    sum += 4
                    i += 1
                elif s[i+1] == 'X':
                    sum += 9
                    i += 1
                else:
                    sum += 1
            elif s[i] == 'V':
                sum += 5
            elif s[i] == 'X':
                if i == len(s) - 1:
                    sum += 10
                elif s[i+1] == 'L':
                    sum += 40
                    i += 1
                elif s[i+1] == 'C':
                    sum += 90
                    i += 1
                else:
                    sum += 10
            elif s[i] == 'L':
                sum += 50
            elif s[i] == 'C':
                if i == len(s) - 1:
                    sum += 100
                elif s[i+1] == 'D':
                    sum += 400
                    i += 1
                elif s[i+1] == 'M':
                    sum += 900
                    i += 1
                else:
                    sum += 100
            elif s[i] == 'M':
                sum += 1000
            i += 1
        return sum


n = 'MCMX'
print(Solution().romanToInt(n))
# 1910
