# 09 - Apr - 2020

# Trapping Rainwater

# You have a landscape, in which puddles can form.
# You are given an array of non-negative integers representing the elevation at each location.
# Return the amount of water that would accumulate if it rains.
#
# For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
#        X
#    X███XX█X
#  X█XX█XXXXXX
# [0,1,0,2,1,0,1,3,2,1,2,1]

def capacity(arr):
  # Fill this in.
    left, right = -1, -1
    cap = 0
    for i in range(1, len(arr)-1):
        a = max(arr[0:i])
        b = max(arr[i+1:])
        if (min(a,b) - arr[i]) > 0:
            cap += (min(a,b) - arr[i])
    return cap

print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6