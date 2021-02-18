'''
934. Shortest Bridge
Medium

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:

Input: A = [[0,1],[1,0]]
Output: 1
Example 2:

Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

2 <= A.length == A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
'''

from collections import deque
from typing import List


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def dfs(self, A, i, j, q, vis,):
        vis[i][j] = True
        q.append((i, j))
        row = [0, 1, 0, -1]
        col = [1, 0, -1, 0]

        for r, c in zip(row, col):
            nRow = i + r
            nCol = j + c
            if self.isValid(A, nRow, nCol) and not vis[nRow][nCol] and A[nRow][nCol] == 1:
                vis[nRow][nCol] = True
                self.dfs(A, nRow, nCol, q, vis)

    def shortestBridge(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        q = deque()
        found = False
        vis = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    self.dfs(A, i, j, q, vis)
                    found = True
                    break
            if found:
                break

        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                row = [1, 0, -1, 0]
                col = [0, 1, 0, -1]
                for r, c in zip(row, col):
                    nRow = i + r
                    nCol = j + c
                    if self.isValid(A, nRow, nCol) and not vis[nRow][nCol]:
                        if A[nRow][nCol] == 1:
                            return level
                        q.append((nRow, nCol))
                        vis[nRow][nCol] = True
            level += 1

        return -1


class Solution2:
    def shortestBridge(self, A: List[List[int]]) -> int:
        def dfs(x, y):
            n = len(A)
            A[x][y] = 2
            for dx, dy in direction:
                i, j = x + dx, y + dy
                if i == -1 or j == -1 or i == n or j == n:
                    continue
                if A[i][j] in (-1, 2):
                    continue
                if A[i][j] == 0:
                    A[i][j] = -1
                    que.append((i, j, 0))
                else:
                    dfs(i, j)

        def paint_one_island():
            n = len(A)
            for i in range(n):
                for j in range(n):
                    if A[i][j] == 0:
                        continue
                    dfs(i, j)
                    return

        n = len(A)
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        que = deque()
        paint_one_island()

        while que:
            x, y, step = que.popleft()
            for dx, dy in direction:
                i, j = x + dx, y + dy
                if i == -1 or j == -1 or i == n or j == n:
                    continue

                if A[i][j] == 1:
                    return step + 1
                if A[i][j] in (-1, 2):
                    continue
                A[i][j] = -1
                que.append((i, j, step + 1))
