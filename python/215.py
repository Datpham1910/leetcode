"""
215. Kth Largest Element in an Array
Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

    def findKthLargest1(self, nums: List[int], k: int) -> int:   
        return (heapq.nlargest(k, nums))[-1]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heap = []
        if not nums:
            return 0
        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)

if __name__ == "__main__":
    print(Solution().findKthLargest1([3,2,3,1,2,4,5,5,6], k = 4))
