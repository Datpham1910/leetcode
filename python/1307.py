"""
1307. Verbal Arithmetic Puzzle
Hard

Given an equation, represented by words on left side and the result on right side.

You need to check if the equation is solvable under the following rules:

Each character is decoded as one digit (0 - 9).
Every pair of different characters they must map to different digits.
Each words[i] and result are decoded as one number without leading zeros.
Sum of numbers on left side (words) will equal to the number on right side (result). 
Return True if the equation is solvable otherwise return False.

Example 1:

Input: words = ["SEND","MORE"], result = "MONEY"
Output: true
Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
Example 2:

Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
Output: true
Explanation: Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
Example 3:

Input: words = ["THIS","IS","TOO"], result = "FUNNY"
Output: true
Example 4:

Input: words = ["LEET","CODE"], result = "POINT"
Output: false
 

Constraints:

2 <= words.length <= 5
1 <= words[i].length, result.length <= 7
words[i], result contain only uppercase English letters.
The number of different characters used in the expression is at most 10.
"""
from typing import List

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        """
        The idea is to use backtracking to try all possible values column wise.
        We go column by column and for each column we go row by row and start assigning values.

        The first thing i do is, make sure to reverse the words and result. so that i = 0 , represents LSB.
        Then start assigning for each column. column 0 is the LSB, and column 1 is the next one and so on.

        In my progrram solve(i, j, carry) => i represents which column for this iteration and j represents which word in the current iteration we are trying to assign values. carry represents the carry over value from the previous column.

        With this structure the remaining part is simply to assign values to all the word characters of a particular column from the unassigned set of (0 - 9) and if the column assignment is over, we check if the summation of that column holds true by comparing with the corresponding character in the Result (if that char in result is already assigned, or else we assign the current sum value to the corresponding char in result). Then we proceed to the next column, starting with word 0.

        Couple of things to take care of;
        a) careful not to assign 0 for the first letter of a word
        b) when trying to assign a particular column of a particular word, make sure that word is long enough.
        """
    def isSolvable(self, words: List[str], result: str) -> bool:
        n = len(result)
        if max(len(w) for w in words) > n:
            return False
        
        level = [[w[-k - 1] for w in words if k < len(w)] for k in range(n)]
        level_set = [set(level[k]) | {result[-k - 1]} for k in range(n)]
        leading = set(w[0] for w in words) | {result[0]}
        val = {k: None for k in set.union(set(result), *(set(w) for w in words))}
        used = set()
        
        def search(k, carry):
            if k == n:
                return carry == 0
            
            for c in level_set[k]:
                if val[c] is None:
                    for v in range(c in leading, 10):
                        if v not in used:
                            val[c] = v
                            used.add(v)
                            if search(k, carry):
                                return True
                            val[c] = None
                            used.remove(v)
                    return False
                
            s = sum(val[c] for c in level[k]) + carry
            if s % 10 != val[result[-k - 1]]:
                return False
            return search(k + 1, s // 10)

        return search(0, 0)