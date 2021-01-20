"""
* 1047. Remove All Adjacent Duplicates In String
* Easy
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 

Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.
"""
import string


class Solution:
    def removeDuplicates(self, S: str) -> str:
        duplicates = [2*ch for ch in string.ascii_lowercase]
        prev_length = 0
        while prev_length != len(S):
            prev_length = len(S)
            for d in duplicates:
                S = S.replace(d, '')
        return S

    def removeDuplicates2(self, S: str) -> str:
        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)


if __name__ == "__main__":
    print(Solution().removeDuplicates("abbaca"))
