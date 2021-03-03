"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

from typing import List

class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

    def generateParenthesis1(self, n: int) -> List[str]:
        cache = [set() for _ in range(n + 1)]
        for i in range(1, n + 1):
            if i == 1:
                cache[i].add("()")
            else:
                for j in range(1, i // 2 + 1):
                    for a in cache[j]:
                        for b in cache[i - j]:
                            cache[i].add(a + b)
                            cache[i].add(b + a)
                            if j == 1:
                                cache[i].add("(" + b + ")")
        return cache[-1]