"""
378. Kth Smallest Element in a Sorted Matrix
Medium

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return heapq.nsmallest(k, heapq.merge(*matrix))[-1]

    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        l = []
        for item in matrix:
            for item1 in item:
                l.append(item1)
        m = sorted(l)
        return m[k-1]

    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        if (matrix is None) or (matrix[0] is None):
            return None

        if len(matrix) == 1:
            return matrix[0][0]

        if k == 1:
            return matrix[0][0]

        h = []
        for row in matrix:
            heapq.heappush(h, row)
        counter = 0
        while k != counter:
            r = heapq.heappop(h)
            ele = r.pop(0)
            counter += 1
            if k == counter:
                return ele
            else:
                if r:
                    heapq.heappush(h, r)
                    heapq.heapify(h)

        return 0


if __name__ == "__main__":
    Solution().kthSmallest(matrix=[
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ],
        k=8,)
