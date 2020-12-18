from typing import List
"""
1004. Max Consecutive Ones III
*Medium*

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.
"""

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        n = len(A)

        for right in range(n):
            K -= 1 - A[right]
            if K < 0:
                K += 1- A[left]
                left +=1
                
        return right - left + 1
        