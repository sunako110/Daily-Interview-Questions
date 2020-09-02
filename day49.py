# 27 - Apr - 2020

# Room scheduling

# You are given an array of tuples (start, end) representing time intervals for lectures.
# The intervals may be overlapping. Return the number of rooms that are required.
#
# For example. [(30, 75), (0, 50), (60, 150)] should return 2.

def schedule(intervals):
    intervals.sort()
    merge = [intervals[0]]
    for i in range(1,len(intervals)):
        for j in range(len(merge)):
            if merge[j][1] <= intervals[i][0]:
                merge[j] = (merge[j][0], intervals[i][1])
                break
            else:
                if j == len(merge) - 1:
                    merge.append(intervals[i])
                else:
                    continue
    return len(merge)

list = [(30, 75), (0, 50), (60, 150)]
print(schedule(list))