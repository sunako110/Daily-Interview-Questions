# 14 - May - 2020

# H-Index

# The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a scholar.
# The definition of the h-index is if a scholar has at least h of their papers cited h times.
#
# Given a list of publications of the number of citations a scholar has, find their h-index.
#
# Example:
# Input: [3, 5, 0, 1, 3]
# Output: 3
# Explanation:
# There are 3 publications with 3 or more citations, hence the h-index is 3.

def hIndex(publications):
    # Fill this in.
    if max(publications) == 0:
        return 0
    dp = [1] * len(publications)
    for i in range(1, len(publications)):
        count = 0
        for j in range(0,i+1):
            if publications[j] >= dp[i-1] + 1:
                count += 1
        if count == dp[i - 1] + 1:
            dp[i] = count
        else:
            dp[i] = dp[i - 1]
    print(dp)
    return dp[-1]

print(hIndex([5, 3, 3, 1, 0]))
# 3