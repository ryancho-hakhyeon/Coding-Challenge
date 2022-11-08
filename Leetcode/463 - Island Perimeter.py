# You are given row x col grid representing a map where grid[i][j] = 1
# represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes",
# meaning the water inside isn't connected to the water around the island.
# One cell is a square with side length 1.
# The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        perimeter = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    perimeter += 4

                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 1
                    if r < row - 1 and grid[r + 1][c] == 1:
                        perimeter -= 1
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 1
                    if c < col - 1 and grid[r][c + 1] == 1:
                        perimeter -= 1

        return perimeter


obj = Solution()

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(obj.islandPerimeter(grid))    # Output: 16

grid = [[1]]
print(obj.islandPerimeter(grid))    # Output: 4

grid = [[1,0]]
print(obj.islandPerimeter(grid))    # Output: 4
