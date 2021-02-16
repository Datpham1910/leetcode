'''
1254. Number of Closed Islands
Medium

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands. 

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
'''
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        island_count = 0

        def dfs_island(grid, i, j):
            # explore island in dfs manner.

            # basically any other cell is valid boundary
            if grid[i][j] != 0:
                return grid, True

            # if island touches the boundary of the grid, then its an invalid island
            if i == 0 or i == (len(grid)-1) or j == 0 or j == len(grid[0])-1:
                return grid, False

            # update the grid[i][j] to denote visited
            grid[i][j] = 2

            # DFS search in all directions
            grid, T = dfs_island(grid, i-1, j)
            grid, B = dfs_island(grid, i+1, j)
            grid, L = dfs_island(grid, i, j-1)
            grid, R = dfs_island(grid, i, j+1)

            # if all boundaries are valid, then current will return valid response
            # else, the current cell has an invalid boundary
            valid = False
            if T and B and L and R:
                valid = True
            return grid, valid

        for i in range(m):
            for j in range(n):

                if grid[i][j] != 0:
                    continue

                # explore island and update count only if it is a valid island
                grid, valid = dfs_island(grid, i, j)
                if valid:
                    island_count += 1

        return island_count
