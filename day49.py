# 27 - Apr - 2020

# Room scheduling

# You are given an array of tuples (start, end) representing time intervals for lectures.
# The intervals may be overlapping. Return the number of rooms that are required.
#
# For example. [(30, 75), (0, 50), (60, 150)] should return 2.

import heapq
def schedule(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort()
    heap = [(intervals[0][1],intervals[0][0])]
    heapq.heapify(heap)
    for i in range(1,len(intervals)):
        curr = heapq.heappop(heap)
        if curr[0] <= intervals[i][0]:
            new_curr = (intervals[i][1],curr[1])
            heapq.heappush(heap,new_curr)
        else:
            heapq.heappush(heap,(intervals[i][1], intervals[i][0]))
            heapq.heappush(heap, curr)
    return len(heap)

list = [(30, 75), (0, 50), (60, 150)]
print(schedule(list))