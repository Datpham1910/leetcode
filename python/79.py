"""
79. Word Search
Medium

Given an m x n gird of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Note: There will be some test cases with a board or a word larger than constraints to test if your solution is using pruning.

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, y, x, visit):
            if len(word) == 0:
                return True
            elif len(word) == 1:
                return board[y][x] == word
            else:
                if board[y][x] == word[0]:
                    visit[y][x] = True
                    if y > 0 and not visit[y-1][x]:
                        if dfs(board, word[1:], y-1, x, visit):
                            return True
                    if y < height-1 and not visit[y+1][x]:
                        if dfs(board, word[1:], y+1, x, visit):
                            return True
                    if x > 0 and not visit[y][x-1]:
                        if dfs(board, word[1:], y, x-1, visit):
                            return True
                    if x < width-1 and not visit[y][x+1]:
                        if dfs(board, word[1:], y, x+1, visit):
                            return True
                    visit[y][x] = False
                    return False
                else:
                    return False
                    
        height = len(board)
        width = len(board[0])
        visit = [[False]*width for _ in range(height)]
        if height == 1 and width == 0:
            return len(word) == 0
        for i in range(height):
            for j in range(width):
                if dfs(board, word, i, j, visit):
                    return True
        return False
