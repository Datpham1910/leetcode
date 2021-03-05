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
