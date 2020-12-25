"""
856. Score of Parentheses
Medium

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
"""

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = bal = 0
        for i, x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i-1] == '(':
                    ans += 1 << bal
        return ans
        
    def scoreOfParentheses1(self, S: str) -> int:
        stack = []
        res = 0
        for ch in S:
            if ch == '(':
                stack.append(0)
            else:
                last = stack.pop()
                if stack:
                    stack[-1] += 2 * last or 1
                else:
                    res += 2 * last or 1
        return res