# 16 - Mar - 2020

# Number of Ways to Climb Stairs

# You are given a positive integer N which represents the number of steps in a staircase.
# You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

def staircase(n):
    # Fill this in.
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return staircase(n-1) + staircase(n-2)

print(staircase(4))
# 5
print(staircase(5))
# 8
