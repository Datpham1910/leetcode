"""
1162. As Far from Land as Possible
Medium

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
from typing import List
from itertools import product 

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        The idea is completly the same as 542. 01 Matrix.
        We maintain a dp table, the entries in the dp table represent the distance to the nearest '1' + 1, why +1? Will explain this in a second.
        We traverse the grid 2 times, first from left up -> bottom right, second bottom right -> left up.
        In the first loop, we update the minimum distance to reach a '1' from the current position either keep going left or going upward. Here's a small trick, 
        i pick 201 as the max value, cuz per the problem description, the # of rows won't exceed 100, so the length of longest path in the matrix will not exceed 200.
        Say, a matrix A, after the first loop, it will become

        [1, 0, 0]      [1, 2, 3]
        [0, 0, 0]  ->  [2, 3, 4]
        [0, 0, 1]      [3, 4, 1]
        please note that this is not the real distance

        In the second loop, we go from bottom right to up left to update the min distance from another side. At the end, please not that res is not the value we want, if there's no '1's in the matrix, all the entry will be set to 201 in such a case, we should return -1 instead of 201; if there are '1's in the matrix, as mentioned at the begining, res is the maximum distance + 1, so we need res-1.

        [1, 2, 3]    [1, 2, 3]  real distance [0, 1, 2]
        [2, 3, 4] -> [2, 3, 2]        ->      [1, 2, 1]
        [3, 4, 1]    [3, 2, 1]        -1      [2, 1, 0]
        the maximum value in the table is 3, this means the answer is 3 - 1 = 2.
        time/space: O(nm)/O(1)
        """
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, res = len(grid), 0
        land = {(i, j) for i, j in product(range(n), range(n)) if grid[i][j]}
        water = {(i, j) for i, j in product(range(n), range(n)) if not grid[i][j]}
        while water:
            if not land: return -1
            land = {(x, y) for i, j in land for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)) if (x, y) in water}
            water -= land
            res += 1
        return res or -1