"""
909. Snakes and Ladders
Medium

On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board, and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:

You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square x, consists of the following:

You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
(This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations, regardless of the size of the board.)
If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or ladder is board[r][c].

Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at `3`, because you do not continue moving to `4`.)

Return the least number of moves required to reach square N*N.  If it is not possible, return -1.

Example 1:

Input: [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
Note:

2 <= board.length = board[0].length <= 20
board[i][j] is between 1 and N*N or is equal to -1.
The board square with number 1 has no snake or ladder.
The board square with number N*N has no snake or ladder.
"""
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)
        visited = [False] * (N * N)
        a = []
        s = -1

        # Translate the board into an array a, with index from
        # 0 to N * N - 1
        for i in range(N - 1, -1, -1):
            j = 0
            s = s * (-1)
            while j < N:
                if s == 1:
                    a.append(board[i][j])
                else:
                    a.append(board[i][N - 1 - j])
                j += 1

        # BFS part
        q = []
        q.append(0)
        visited[0] = True
        res = 0
        while len(q) > 0:
            size_q = len(q)
            for i in range(0, size_q, 1):
                j = q.pop(0)
                if j == N**2 - 1:
                    return res
                for k in range(1, 7):
                    if j + k > N**2 - 1:
                        continue
                    if a[j + k] == -1:
                        p = j + k
                    else:
                        p = a[j + k] - 1
                    if visited[p]:
                        continue
                    visited[p] = True
                    q.append(p)
            res += 1
        return -1

    def snakesAndLadders1(self, board: List[List[int]]) -> int:
        n = len(board)
        q, visited = {1}, set()
        goal = n*n
        flatboard = [0]
        for i, row in enumerate(board[::-1]):
            flatboard.extend(row if i % 2 == 0 else row[::-1])
        res = 0
        while q:
            next_q = set()
            visited |= q
            for sq in q:
                for x in range(sq+1, min(goal+1, sq + 7)):
                    next_q.add(flatboard[x] if flatboard[x] != -1 else x)
                if goal in next_q:
                    return res + 1
            q = next_q - visited
            res += 1
        return -1
