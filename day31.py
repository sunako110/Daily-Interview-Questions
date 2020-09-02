# 03 - Apr - 2020

# Merge Overlapping Intervals

# You are given an array of intervals - that is, an array of tuples (start, end).
# The array may not be sorted, and could contain overlapping intervals.
# Return another array where the overlapping intervals are merged.
#
# For example:
# [(1, 3), (5, 8), (4, 10), (20, 25)]
#
# This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

def merge(intervals):
    # Fill this in.
    intervals.sort()
    merge = [intervals[0]]
    index = 0
    for i in range(1,len(intervals)):
        if merge[index][1] >= intervals[i][0]:
            merge[index] = (min(intervals[index][0], intervals[i][0]),max(intervals[index][1], intervals[i][1]))
        else:
            index += 1
            merge.append(intervals[i])
    # if intervals[i][1] > intervals[i-1][1]:
    #         merge.append(intervals[i])
    return merge



    return intervals

print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
print(merge([(6, 8), (1, 9), (2, 4), (4, 7)]))
