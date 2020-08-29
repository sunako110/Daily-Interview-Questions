# 16 - Apr - 2020

# Longest Substring With K Distinct Characters

# You are given a string s, and an integer k.
# Return the length of the longest substring in s that contains at most k distinct characters.
#
# For instance, given the string:
# aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.

def longest_substring_with_k_distinct_characters(s, k):
    # Fill this in.
    n = 1
    count = []
    if len(s) == 0:
        return
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            n += 1
        else:
            count.append(n)
            n = 1
    count.append(n)
    max = 0
    sum = 0
    i = k
    for num in count:
        i -= 1
        sum += num
        if i == 0:
            if sum > max:
                max = sum
            sum = 0
            i = k

    return max

print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
