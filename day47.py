# 24 - Apr - 2020

# Minimum Removals for Valid Parenthesis

# You are given a string of parenthesis.
# Return the minimum number of parenthesis that would need to be removed in order to make the string valid.
# "Valid" means that each open parenthesis has a matching closed parenthesis.
#
# Example:
#
# The following input should return 1.
#
# "()())()"

def count_invalid_parenthesis(string):
    # Fill this in.
    if len(string) == 0:
        return 0
    else:
        if string[0] == ")":
            return 1 + count_invalid_parenthesis(string[1:]) if len(string) > 1 else 1
        elif string[0] == "(":
            j = string.find(")",1)
            if j < 0:
                return 1 + count_invalid_parenthesis(string[1:])
            if j + 1 == len(string):
                return count_invalid_parenthesis(string[1:j])
            else:
                return count_invalid_parenthesis(string[1:j] + string[j+1:])


print(count_invalid_parenthesis("()())()"))
# 1