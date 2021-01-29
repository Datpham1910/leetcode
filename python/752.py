"""
752. Open the Lock
Medium

1401

55

Add to List

Share
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1
 

Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
"""

from typing import List
from queue import Queue


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        Althouth using bidirectional BFS can solve it fast,
        the lock has an interesting pattern and I saw no one talks about it.
        If using the pattern, it will far faster than BFS in this task.

        The key point is the deadends only can affect the neighbors of target.
        The num of neighbors of last move is always 8 because four digits can only be added +1 or -1 to move.
        If not all the 8 neighbors in deadends, there are solutions.

        Next, how can we count the steps?
        It's about the distance as we know.
        The distance of target D can be calculated by 4 digits eazily.
        As for the 8 neighbors, they are only two distances, D+1 or D-1.

        Therefore, if we have live neighbors, we only have two possible answers.
        One is we can arrive any neighbors of distance D-1, and the answer will be the distance of target D.
        The other is we can arrive any neighbors of distance D+1, and the answer will be the distance of target D+2
        because we have to arrive D+1 first and go to target.

        Take Example 1 for example.

        deadends = ["0201","0101","0102","1212","2002"], 
        target = "0202"
        neighbors of target = {'0102', '9202', '0212', '0292', '0302', '0203', '0201', '1202'}
        the distance of neighbors :  [3, 5, 5, 5, 5, 5, 3, 5]
        After deleting deadends:
        live neighbors of target {'9202', '0212', '0292', '0302', '0203', '1202'}
        the distance of target : 2+2 = 4
        the distance of neighbors : {5, 5, 5, 5, 5, 5}
        Therefore, we can get result is 4+2 = 6 steps.

        The following copied code is from some great writer.
        I added some comments to be more readable.
        """
        deadends = set(deadends)
        # exception, all deadends surround "0000"
        constrain = {"1000", "0100", "0010", "0001", "9000", "0900", "0090", "0009"}
        if deadends == constrain:
            return -1
        if '0000' in deadends:
            return -1
        if target == "0000":
            return 0

        # func of distance
        def dist(code):
            return sum(min(int(c), 10-int(c)) for c in code)

        def neighbors(code):
            for i in range(4):
                x = int(code[i])
                yield code[:i] + str((x - 1) % 10) + code[i + 1:]
                yield code[:i] + str((x + 1) % 10) + code[i + 1:]

        # delete deadends in 8 neighbors
        last_moves = set(neighbors(target)) - deadends
        if not last_moves:
            return -1

        # calculate distance of target
        ans = dist(target)
        for code in last_moves:
            # if any last move has less distance than target,
            # it means that code can approach target no more steps than target
            if dist(code) < ans:
                return ans
        return ans + 2

    def openLock2(self, deadends: List[str], target: str) -> int:
        if('0000' in deadends):
            return -1
        if(target == '0000'):
            return 0
        visited = [False]*10000
        for i in deadends:
            visited[int(i)] = True
        target = int(target)
        q = Queue()
        q.put(0)
        visited[0] = True
        dep = 0
        while(not q.empty()):
            for i in range(q.qsize()):
                cur = q.get()
                res = cur
                for div in [1000, 100, 10, 1]:
                    pos = int(res / div)

                    if(pos == 9):
                        t = cur - 9 * div
                    else:
                        t = cur + div
                    if(t == target):
                        return dep + 1
                    if(visited[t] == False):
                        q.put(t)
                        visited[t] = True

                    if(pos == 0):
                        t = cur + 9 * div
                    else:
                        t = cur - div
                    if(t == target):
                        return dep + 1
                    if(visited[t] == False):
                        q.put(t)
                        visited[t] = True
                    res = res % div
            dep += 1
        return -1

    def openLock3(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        cannot_move = {"1000", "0100", "0010", "0001", "9000", "0900", "0090", "0009"}
        if cannot_move == cannot_move & set(deadends) or "0000" in deadends:
            return -1

        ret = 0
        block = 1
        fast = 1
        for i in range(len(target)):
            val = int(target[i])
            up = (val+1) % 10
            down = (val+9) % 10
            up_str = str(target[:i]) + str(up) + str(target[i+1:])  # check.add(deadends[:i] + str(up) + deadends[i+1:])
            down_str = str(target[:i]) + str(down) + str(target[i+1:])  # check.add(deadends[:i] + str(down) + deadends[i+1:])
            if not (up_str in deadends and down_str in deadends):
                block = 0
            if val != 0:
                if val < 5:
                    if down_str not in deadends:
                        fast = 0
                elif val > 5:
                    if up_str not in deadends:
                        fast = 0
                else:
                    if down_str not in deadends or up_str not in deadends:
                        fast = 0
            ret = ret + min(val, 10-val)

        if block == 1:
            return -1
        if fast == 1:
            ret = ret + 2

        return ret
