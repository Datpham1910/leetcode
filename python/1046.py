"""
1046. Last Stone Weight
Easy

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            l = -heapq.heappop(stones)
            r = -heapq.heappop(stones)
            if l != r:
                heapq.heappush(stones, -abs(l - r))
        return abs(stones[0]) if len(stones) else 0

    def lastStoneWeight1(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        heapq.heapify(stones)
        while(len(stones)>1):
            y=-1*heapq.heappop(stones)
            x=-1*heapq.heappop(stones)
            if(x<y):
                heapq.heappush(stones,x-y)
        if(stones):
            return -1*stones[0]

        # time complexity : O(NlogN)
        # extra space complexity: O(1)
        return 0
if __name__ == "__main__":
    print(Solution().lastStoneWeight([2,7,4,1,8,1]))
