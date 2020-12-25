"""
503. Next Greater Element II
Medium

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        from collections import deque
        right = deque() # Doubly Ended Queue
        n = len(nums)
        res = [-1]*n
        pending = deque()
        for i in range(n-1, -1, -1):
            while right and nums[right[-1]] <= nums[i]:
                right.pop()
            if right:
                res[i] = nums[right[-1]]
            else:
                pending.append(i)
            right.append(i)
        i = 0
        while pending and i < pending[0]:
            while i < pending[0] and nums[i] <= nums[pending[0]]:
                i += 1
            if i < pending[0]:
                res[pending.popleft()] = nums[i]
        return res


if __name__ == "__main__":
    print(Solution().nextGreaterElements([1, 2, 1]))
