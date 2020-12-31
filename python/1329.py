"""
1329. Sort the Matrix Diagonally
Medium

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Example 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 
Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
"""
from typing import List
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                x=i
                y=j
                while(mat[x][y] < mat[x-1][y-1]):
                    temp = mat[x][y]
                    mat[x][y] = mat[x-1][y-1]
                    mat[x-1][y-1] = temp
                    x-=1
                    y-=1
                    if x==0 or y==0:
                        break
                
        return mat

if __name__ == "__main__":
    print(Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
