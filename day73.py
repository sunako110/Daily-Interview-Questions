# 21 - May - 2020

# No Adjacent Repeating Characters

# Given a string, rearrange the string so that no character next to each other are the same.
# If no such arrangement is possible, then return None.
#
# Example:
# Input: abbccc
# Output: cbcbca


def rearrangeString(s):
    # Fill this in.
    result = str(s[0])
    for c in s[1:]:
        if c != result[0] and c != result[-1]:
            result += c
        elif c != result[0]:
            result = c + result
        elif c != result[-1]:
            result += c
        elif len(s) > 2:
            for i in range(1, len(result)):
                if c != result[i] and c != result[i-1]:
                    result = result[:i] + c + result[i:]
                    break
        else:
            return None
    return result


print(rearrangeString('abbccc'))
# cbcabc