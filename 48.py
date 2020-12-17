"""
48. Rotate Image
*Medium*
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)

        for i in range(length):
            j = i
            while j < length:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                j += 1
        for i in range(length):
            j = 0
            while j < length / 2:
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][length - 1 - j]
                matrix[i][length - 1 - j] = temp
                j += 1
        return matrix

print(Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))