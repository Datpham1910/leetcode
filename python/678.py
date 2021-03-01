"""
678. Valid Parenthesis String
Medium

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        right = 0
        for c in s:
            if c == "(":
                left += 1
                right += 1

            elif c == ")":
                left = max(left-1,0)
                right -= 1
            elif c == "*":
                left = max(left-1,0)
                right += 1
            if right < 0:
                    return False
                
        if left<=0 and 0<=right:
            return True
        return False

    def checkValidString1(self, s: str) -> bool:
        dp = 1
        for i,c in enumerate(s):
            if c=='(':
                dp = dp << 1
            elif c == ')':
                dp = dp >> 1
            else:
                dp = (dp << 1) | (dp >> 1) | dp
        return dp %2
