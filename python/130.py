'''
130. Surrounded Regions
Medium

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

from typing import List
import collections

class Solution:
    def solve1(self, board):
        if not board or not board[0]:
            return
        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                self.dfs(board, i, j)
        for i in range(len(board)):
            for j in [0, len(board[0])-1]:
                self.dfs(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '.':
                    board[i][j] = 'O'

    def dfs(self, board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
            board[i][j] = '.'
            self.dfs(board, i+1, j)
            self.dfs(board, i-1, j)
            self.dfs(board, i, j+1)
            self.dfs(board, i, j-1)

    # BFS
    def solve2(self, board):
        queue = collections.deque([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "O":
                board[r][c] = "."
                queue.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == ".":
                    board[r][c] = "O"


    def solve2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        
        self.ROWS = len(board)
        self.COLS = len(board[0])
        
        # Step1: retrive all border cells 
        from itertools import product  # Cartesian product 
        borders = list(product(range(self.ROWS), [0, self.COLS - 1])) + list(product([0,self.ROWS - 1], range(self.COLS)))
            
            
        # Step 2. Mark the 'escaped' cells with any placeholder e.g 'E'
        for row,col in borders:
            self.DFS(board, row, col)
            
        
        # Step 3. flip the captured cells ('O' -> 'X') and the escpated one ('E' - O)
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == 'O': board[r][c] = 'X' # captured 
                elif board[r][c] == 'E': board[r][c] = 'O' # escaped 
        
        
    def DFS(self, board, row, col): # Four direction
        if board[row][col] != 'O':
            return 
        board[row][col] = 'E'
        if col < self.COLS - 1: self.DFS(board, row, col + 1) # depth first: defined as the first direction 
        if row <self.ROWS - 1 : self.DFS(board, row + 1, col)
        if col >0 : self.DFS(board, row, col - 1)
        if row >0: self.DFS(board, row - 1, col)