# 23 - Apr - 2020

# Find the Number of Islands

# Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks),
# count the number of islands present in the grid.
# The definition of an island is as follows:
# 1.) Must be surrounded by water blocks.
# 2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
# Assume all edges outside of the grid are water.
#
# Example:
# Input:
# 10001
# 11000
# 10110
# 00000
#
# Output: 3

class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
          return False
        return True

    def isSafe(self, visited, grid, r, c):
        return self.inRange(grid, r, c) and not visited[r][c] and grid[r][c]

    def numIslands(self, grid):
        # Fill this in.
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == False and grid[i][j] == 1:
                    self.DFS(i, j, visited, grid)
                    count += 1
        return count

    def DFS(self,row,col,visited,grid):
        row_shift = [-1, 0, 0, 1]
        col_shift = [0, -1, 1, 0]
        visited[row][col] = True

        for k in range(4):
            if self.isSafe(visited, grid, row + row_shift[k], col + col_shift[k]):
                self.DFS(row + row_shift[k], col + col_shift[k], visited, grid)



grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]
print(Solution().numIslands(grid))
# 3