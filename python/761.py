"""
761. Special Binary String
Hard

Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.
Given a special string S, a move consists of choosing two consecutive, non-empty, special substrings of S, and swapping them. (Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.)

At the end of any number of moves, what is the lexicographically largest resulting string possible?

Example 1:
Input: S = "11011000"
Output: "11100100"
Explanation:
The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.
Note:

S has length at most 50.
S is guaranteed to be a special binary string as defined above.
"""
import queue
class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        return self.visit(0, S) 

    def visit(self,index: int, s: str) -> str:
        if s[0] == '0': return ""
        tokens = queue.PriorityQueue()

        token = ""
        while(index < len(s) and s[index] == '1'):
            token = "1"+ self.visit(index+1, s)+"0"
            index+= len(token)
            tokens.put(token)
        
        result = ""
        while (tokens.qsize() > 0):
            result = tokens.get()+result
        return result

    def makeLargestSpecial1(self, S: str) -> str:
        stack = []
        cache = [[]] # each entry is a list of special string
        
        for c in S:
            # push into stack
            if c == '1': 
                stack.append(1)
                if len(stack) >= len(cache):
                    cache.append([])
                continue
                
            # pop and resolve by sort, merge & wrap
            cache[-1].sort(reverse=True)
            tmp = '1' + ''.join(cache.pop()) + '0'
            cache[-1].append(tmp)
            stack.pop()
            
        cache[0].sort(reverse=True)
        return ''.join(cache[0])

if __name__ == "__main__":
    print(Solution().makeLargestSpecial1("11011000"))
