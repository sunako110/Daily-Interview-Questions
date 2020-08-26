# 04 - Mar -2020

# Longest Substring Without Repeating Characters

class  Solution:
    def lengthOfLongestSubstring(self, s):
        # Fill this in.
        max = 0
        start_pos = 0
        for i in range(1,len(s)):
            if s[i] in s[start_pos:i]:
                if i - start_pos > max:
                    max = i - start_pos
                start_pos = s[start_pos:i].find(s[i]) + start_pos + 1
        return max if max != 0 else len(s)


print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10

