"""
1391. Check if There is a Valid Path in a Grid
Medium

Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.


You will initially start at the street of the upper-left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

Example 1:

Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
Example 4:

Input: grid = [[1,1,1,1,1,1,3]]
Output: true
Example 5:

Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
Output: true
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
"""
from typing import List

'''
w: graph
h: link the cell one by one, for each type of street, there are two ends
    we need to consider what type of streets can be connected for each end
    use idx to present each end of street
'''
import collections
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        connected = {1: {0: [1, 3, 5], 1: {1, 4, 6}}, 2: {0: [2, 3, 4], 1: [2, 5, 6]}, 
                     3: {0: [1, 4, 6], 1: {2, 5, 6}}, 4: {0: [1, 3, 5], 1: [2, 5, 6]},
                     5: {0: [1, 6, 4], 1: [2, 4, 3]}, 6: {0: [2, 4, 3], 1: [3, 1, 5]}}
        
        directions = {1: [(0, 1), (0, -1)], 2: [(-1, 0), (1, 0)], 3: [(0, -1), (1, 0)],
                      4: [(0, 1), (1, 0)], 5: [(0, -1), (-1, 0)], 6: [(-1, 0), (0, 1)]}
        
        
        seen = set()
        deque = collections.deque([(0,0)])
        
        while deque:
            #print(deque)
            x, y = deque.popleft()
            seen.add((x, y))
            
            if x == m-1 and y == n-1:
                return True
            
            street = grid[x][y]
            for idx, (dx, dy) in enumerate(directions[street]):
                nx = x+dx
                ny = y+dy
                if 0<=nx<=m-1 and 0<=ny<=n-1 and (nx, ny) not in seen and grid[nx][ny] in connected[street][idx]:
                    deque.append((nx, ny))
                    seen.add((nx, ny))
        
        
        return False

    def try_driving(self, grid, r, c, d) -> bool:
        # create mapping (street, entry) -> (exit, dr, dc)
        DRIVE = { (1, 0): (2, 0, -1), (1, 2): (0, 0, 1),
                  (2, 1): (3, 1, 0), (2, 3): (1, -1, 0),
                  (3, 2): (3, 1, 0), (3, 3): (2, 0, -1),
                  (4, 0): (3, 1, 0), (4, 3): (0, 0, 1),
                  (5, 1): (2, 0, -1), (5, 2): (1, -1, 0),
                  (6, 0): (1, -1, 0), (6, 1): (0, 0, 1) }
        m = len(grid)
        n = len(grid[0])
        while True:
            # check if we've driven out of bounds
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            
            # check if we can enter the cell at r, c
            s = grid[r][c]
            if (s, d) not in DRIVE:
                return False
            
            # check if we've entered the destination
            if r + 1 == m and c + 1 == n:
                return True
            
            # drive along this segment
            d, dr, dc = DRIVE[(s, d)]
            d = (d + 2) % 4
            r += dr
            c += dc
            
            # if we're back at the start, we found a loop
            if r == 0 and c == 0:
                return False
        
    
    def hasValidPath1(self, grid: List[List[int]]) -> bool:
        # try driving into top-left from each direction
        for i in range(4):
            if self.try_driving(grid, 0, 0, i):
                return True
        return False

    def hasValidPath2(self, grid: List[List[int]]) -> bool:
        r, c = len(grid), len(grid[0])
        visited, q = [[0]*c for _ in range(r)], collections.deque([(0, 0)])
        visited[0][0] = 1
        dire = [[(0,-1),(0,1)], [(-1,0),(1,0)], [(0,-1),(1,0)], [(0,1),(1,0)], [(0,-1),(-1,0)], [(0,1),(-1,0)]]
        while q:
            i, j = q.popleft()
            if i == r-1 and j == c-1: return True
            for di, dj in dire[grid[i][j]-1]:
                x, y = i+di, j+dj
                if 0<=x<r and 0<=y<c and not visited[x][y] and (-di, -dj) in dire[grid[x][y]-1]:
                    visited[x][y] = 1; q.append((x, y))
        return False