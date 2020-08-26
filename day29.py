# 01 - Apr - 2020

# Spiral Traversal of Grid

# You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.
#
# Example:
#
# grid = [[1,  2,  3,  4,  5],
#         [6,  7,  8,  9,  10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20]]
#
# The clockwise spiral traversal of this array is:
#
# 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

def matrix_spiral_print(M):
  # Fill this in.
    if not M:
        return
    while M:
        for n in M[0]:
            print(n,end = " ")
        M.pop(0)
        for list in M:
            print(list[-1], end = " ")
            list.pop(-1)
        for i in range(1,len(M[-1])+1):
            print(M[-1][-i], end = " ")
        M.pop(-1)
        for i in range(1,len(M)+1):
            print(M[-i][0], end = " ")
            M[-i].pop(0)
    print ("")

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12