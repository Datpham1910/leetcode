"""
529. Minesweeper
Medium

791

617

Add to List

Share
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

 

Note:

The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.
"""

from typing import List
import collections

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        surround = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]

        def available(x, y):
            return 0 <= x < len(board) and 0 <= y < len(board[0])

        def reveal(board, x, y):
            # reveal blank cell with dfs
            if not available(x, y) or board[x][y] != "E":
                return
            # count adjacent mines
            mine_count = 0

            for dx, dy in surround:
                if available(dx+x, dy+y) and board[dx+x][dy+y] == "M":
                    mine_count += 1

            if mine_count:
                # have mines in adjacent cells
                board[x][y] = str(mine_count)
            else:
                # not adjacent mines
                board[x][y] = "B"
                for dx, dy in surround:
                    reveal(board, dx+x, dy+y)

        if board[x][y] == "M":
            board[x][y] = "X"
        elif board[x][y] == "E":
            reveal(board, x, y)
        return board

    def updateBoard1(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        d = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
        m, n = len(board), len(board[0])

        def dfs(B, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if B[i][j] == 'M':
                B[i][j] = 'X'
            elif B[i][j] == 'E':
                mine = sum(B[i+x][j+y] == 'M' for x, y in d if 0 <= i+x < m and 0 <= j+y < n)
                B[i][j] = mine and str(mine) or 'B'
                for x, y in d * (not mine):
                    dfs(B, i+x, j+y)
            return B

        return dfs(board, *click)

    def updateBoard2(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
        if not board or not board[0] or not click:
            return []

        n, m = len(board), len(board[0])
        queue = collections.deque([click])
        digits = set('1,2,3,4,5,6,7,8,9'.split(','))

        while queue:
            cx, cy = queue.popleft()
            if board[cx][cy] == 'M':
                board[cx][cy] = 'X'
                return board
            if board[cx][cy] == 'B' or board[cx][cy] in digits:
                continue
            cache = []
            for dx, dy in DIR:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if board[nx][ny] == 'M':
                    if board[cx][cy] == 'E':
                        board[cx][cy] = '1'
                    elif board[cx][cy] in digits:
                        board[cx][cy] = str(int(board[cx][cy]) + 1)
                elif board[nx][ny] == 'E':
                    cache.append((nx, ny))

            if board[cx][cy] == 'E':
                board[cx][cy] = 'B'
                queue.extend(cache)

        return board