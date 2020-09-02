# 25 - Apr - 2020

# Group Words that are Anagrams

# Given a list of words, group the words that are anagrams of each other. (An anagram are words made up of the same letters).
#
# Example:
#
# Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
# Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

import collections

def groupAnagramWords(strs):
    # Fill this in.
    ans = collections.defaultdict(list)
    for s in strs:
        # ans[tuple(sorted(s))].append(s)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]