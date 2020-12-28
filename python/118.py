"""
118. Pascal's Triangle
Easy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Accepted
440,824
Submissions
814,257
"""
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]*(i+1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                result[i][j] = result[i-1][j-1]+result[i-1][j]
        return result

if __name__ == "__main__":
    print(Solution().generate(10))
