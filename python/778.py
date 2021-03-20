"""
778. Swim in Rising Water
Hard

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].
"""
from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        while True:
            T, x, y = heapq.heappop(pq)
            res = max(res, T)
            if x == y == N - 1:
                return res
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
                    seen.add((i, j))
                    heapq.heappush(pq, (grid[i][j], i, j))

    def swimInWater1(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], max(grid[0][0], 0), 0, 0)]
        n = len(grid)
        visited = [[0 for j in range(n)] for i in range(n)]
        visited[0][0] = 1
        while len(heap) > 0:
            val, t, x, y = heapq.heappop(heap)
            nxt_coords = []
            if x > 0 and visited[x-1][y] == 0:
                nxt_coords.append((x-1, y))

            if x < n-1 and visited[x+1][y] == 0:
                nxt_coords.append((x+1, y))

            if y > 0 and visited[x][y-1] == 0:
                nxt_coords.append((x, y-1))

            if y < n-1 and visited[x][y+1] == 0:
                nxt_coords.append((x, y+1))

            for new_x, new_y in nxt_coords:
                next_t = max(grid[new_x][new_y], t)
                if new_x == new_y == n-1:
                    return next_t
                visited[new_x][new_y] = 1
                heapq.heappush(heap, (grid[new_x][new_y], next_t, new_x, new_y))

"""
Intuition
We ned to find the path from point (0,0) to (N -1, N - 1). We can move to another 4-directionally adjacent square (up, down, right and left). However, we can only move to the next adjacent square if the value inside that square is less than or equal to t.

Brute Force
We'll do a DFS where we'll traverse all adjacent squares that satisify the requirement value of the next grid <= t. If we cannot move else where from the current grid[row][col], we increase the time t. Below is the implementation:

class Solution(object):
    def dfs(self, grid, t, row, col, visited):
       if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1:
            return 0
        
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return 1
        
        visited.add((row, col))
        
        down = up = right = left = 0
        
        if row + 1 < len(grid) and grid[row + 1][col] <= t and (row + 1, col) not in visited:
            down = self.dfs(grid, t, row + 1, col, visited)
            
        if row - 1 >= 0 and grid[row - 1][col] <= t and (row - 1, col) not in visited:
            up = self.dfs(grid, t, row - 1, col, visited)
            
        if col + 1 < len(grid[0]) and grid[row][col + 1] <= t and (row, col + 1) not in visited:
            right = self.dfs(grid, t, row, col + 1, visited)
            
        if col - 1 >= 0 and grid[row][col - 1] <= t and (row, col - 1) not in visited:
            left = self.dfs(grid, t, row, col - 1, visited)
            
        return down or up or right or left
    
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not len(grid) or not len(grid[0]):
            return 0
        
        t = grid[0][0]
        visited = set()
        while self.dfs(grid, t, 0, 0, visited) == 0:
            t += 1
            visited = set()
        
        return t
At the begining of the program, I initialised t = grid[0][0] and increament it by 1 until I found a path that lead to (N-1, N-1). However, this approach will lead to TLE since in the worst-case, t can be very big and total time complexity become O(N2 * t).
To optimise this, we can use binary search to find the minimum feasible water level. The range of our search will be [0, n*n-1].
below is the DFS + Binary Search approach.

class Solution(object):
    def dfs(self, grid, t, row, col, visited):
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or grid[row][col] > t:
            return 0
        
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return 1
        
        visited.add((row, col))
        
        down = up = right = left = 0
        
        if row + 1 < len(grid) and grid[row + 1][col] <= t and (row + 1, col) not in visited:
            down = self.dfs(grid, t, row + 1, col, visited)
            
        if row - 1 >= 0 and grid[row - 1][col] <= t and (row - 1, col) not in visited:
            up = self.dfs(grid, t, row - 1, col, visited)
            
        if col + 1 < len(grid[0]) and grid[row][col + 1] <= t and (row, col + 1) not in visited:
            right = self.dfs(grid, t, row, col + 1, visited)
            
        if col - 1 >= 0 and grid[row][col - 1] <= t and (row, col - 1) not in visited:
            left = self.dfs(grid, t, row, col - 1, visited)
            
        return down or up or right or left
    
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not len(grid) or not len(grid[0]):
            return 0
        
        N = len(grid)
        t_left = grid[0][0]
        t_right = N * N - 1
        
        while t_left < t_right:
            t_mid = t_left + (t_right - t_left) // 2
            
            visited = set()
            if self.dfs(grid, t_mid, 0, 0, visited):
                t_right = t_mid
            else:
                t_left = t_mid + 1
           
        
        return t_left
Time complexity: O(N2 log N).

Hope this can be insightful, and happy learning!
"""