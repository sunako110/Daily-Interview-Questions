# 18 - Mar - 2020

# Edit Distance

# Given two strings, determine the edit distance between them.
# The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution)
# needed to change one string to the other.

# For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).

def distance(s1, s2):
    # Fill this in.
    # dist = 0
    # print s1, s2
    # if len(s1) == 1 and len(s2) == 1:
    #     if s1[0] != s2[0]:
    #         return 1
    #     else:
    #         return 0
    # if len(s1) == len(s2):
    #     if s1[0] != s2[0]:
    #         dist += 1 + distance(s1[1:], s2[1:])
    #     else:
    #         dist += distance(s1[1:], s2[1:])
    # else:
    #     if s1[0] != s2[0]:
    #         if len(s1) > len(s2) and s2[0] == s1[1]:
    #             dist += 1 + distance(s1[2:], s2[1:])
    #         elif len(s1) < len(s2) and s1[0] == s2[1]:
    #             dist += 1 + distance(s1[1:], s2[2:])
    #         else:
    #             dist += 1 + distance(s1[1:], s2[1:])
    #     else:
    #         dist += distance(s1[1:], s2[1:])
    # return dist
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[0] == s2[0]:
        return distance(s1[1:],s2[1:])
    return 1 + min(distance(s1,s2[1:]),distance(s1[1:],s2),distance(s1[1:],s2[1:]))

print(distance('biting','sitting'))
# 2