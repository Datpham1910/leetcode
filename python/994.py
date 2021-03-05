"""
994. Rotting Oranges
Medium

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid):
        """
        This is graph traversal problem, so here we have a choise: to use dfs or to use bfs. What is asked: minimum number of minutes passed until there is no fresh orange. In graphs it means to find the greatest distance from rotten oranges to any other orange. Usually, if we need to find the distances, we use bfs. So, let me define my variables:

    m and n are dimensions of our grid, also we have queue to run our bfs and also we want to count number of fresh oranges: we need this to check in the end if all oranges become rotten or not.
    We put all rotten oranges coordinates to our queue, so we are going to start from all of them. Also we count number of fresh oranges.
    Define directions we can go: four of them and put levels = 0.
    Now, we traverse our grid, using bfs, using level by level traversal: it means, that each time, when we have some elements in queue, we popleft all of them and put new neighbours to the end. In this way each time we reach line levels += 1, we have nodes with distance which is 1 bigger than previous level. In the end levels - 1 will be our answer, because one time in the end when we do not have anythin to add, levels still be incremented by one.

    Finally, we check if we still have fresh oranges, and if yes, return -1. If not, we need to return max(levels-1, 0), because it can happen, that our queue was empty in the beginning and we do not need to subtract 1.

    Complexity: time complexity is O(mn), because we first traverse our grid to fill queue and found number of fresh oranges. Then we use classical bfs, so each node will be added and removed from queue at most 1 time. Space complexity is also can be O(mn), we can have for example O(mn) rotten oranges in the very beginnig.
        """
        m, n, queue, fresh = len(grid), len(grid[0]), deque(), 0
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 2:
                queue.append((i, j))
            if grid[i][j] == 1:
                fresh += 1
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        levels = 0

        while queue:
            levels += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    if 0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy] == 1:
                        fresh -= 1
                        grid[x+dx][y+dy] = 2
                        queue.append((x+dx, y+dy))

        return -1 if fresh != 0 else max(levels-1, 0)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        timer = 0
        while fresh:
            if not rotting:
                return -1
            rotting = {(i+di, j+dj) for i, j in rotting for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh}
            fresh -= rotting
            timer += 1
        return timer
