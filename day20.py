# 23 - Mar - 2020

# Ways to Traverse a Grid

# You 2 integers n and m representing an n by m grid,
# determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

# Example:
# n = 2, m = 2
#
# This should return 2, since the only possible routes are:
# Right, down
# Down, right.

def num_ways(n, m):
    # Fill this in.
# method 1:
#     return int(factorial(n-1+m-1)/(factorial(n-1)*factorial(m-1)))
#
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     return num * factorial(num-1)

# method 2:
#     count = [[0 for x in range(m)] for y in range(n)]
#
#     for i in range(n):
#         count[i][0] = 1
#     for j in range(m):
#         count[0][j] = 1
#
#     for i in range(1,n):
#         for j in range(1,m):
#             count[i][j] = count[i-1][j] + count[i][j-1]
#
#     return count[n-1][m-1]

# method 3:
    if (m == 1) or (n == 1):
        return 1
    return num_ways(n-1,m) + num_ways(n,m-1)



print(num_ways(2, 2))
# 2