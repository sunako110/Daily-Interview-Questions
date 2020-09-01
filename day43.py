# 20 - Apr - 2020

# Word Ordering in a Different Alphabetical Order

# Given a list of words, and an arbitrary alphabetical order, verify that the words are in order of the alphabetical order.
#
# Example:
# Input:
# words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"
#
# Output: False
# Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'
#
# Example 2:
# Input:
# words = ["zyx", "zyxw", "zyxwy"],
# order="zyxwvutsrqponmlkjihgfedcba"
#
# Output: True
# Explanation: The words are in increasing alphabetical order

def isSorted(words, order):
    # Fill this in.
    for i in range(1, len(words)):
        for j in range(len(words[i-1])):
            if words[i-1][j] != words[i][j]:
                if order.find(words[i-1][j]) > order.find(words[i][j]):
                    return False
    return True

print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))
# True