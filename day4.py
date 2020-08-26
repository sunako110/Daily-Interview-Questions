# 06 - Mar - 2020

# Validate Balanced Parentheses

# Every opening bracket must have a corresponding closing bracket.
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.

# Example:
# Input: "((()))"
# Output: True
#
# Input: "[()]{}"
# Output: True
#
# Input: "({[)]"
# Output: False

class Solution:
  def isValid(self, s):
    # Fill this in.
    str = s
    pos = -1
    for i in range(len(s)):
        if s[i] == "(":
            pos = str.find(")")
            str = str[:pos] + str[pos + 1:]
        elif s[i] == "{":
            pos = str.find("}")
            str = str[:pos] + str[pos + 1:]
        elif s[i] == "[":
            pos = str.find("]")
            str = str[:pos] + str[pos + 1:]
        if pos == -1:
            return False
    return True


# Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))