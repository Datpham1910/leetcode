"""
1221. Split a String in Balanced Strings
Easy

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
 

Constraints:

1 <= s.length <= 1000
s[i] = 'L' or 'R'
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        p, c = 0, 0
        for i in range(0, len(s)):
            if s[i] == 'R':
                p += 1
            else:
                p -= 1
            if p == 0:
                c += 1
        return c

    def balancedStringSplit1(self, s: str) -> int:
        res = 0
        # stack = []
        rc, lc = 0, 0
        for char in s:
            if char == 'R':
                rc += 1
            else:
                lc += 1
            if rc == lc:
                # while stack:
                #     stack.pop()
                rc, lc = 0, 0
                res += 1
        return res

if __name__ == "__main__":
    print(Solution().balancedStringSplit("RLRRLLRLRL"))
