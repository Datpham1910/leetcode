"""
1552. Magnetic Force Between Two Balls
Medium

In universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. 
Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

 

Example 1:


Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. 
The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
 

Constraints:

n == position.length
2 <= n <= 10^5
1 <= position[i] <= 10^9
All integers in position are distinct.
2 <= m <= position.length
"""
from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def fn(d):
            """Return True if d is a feasible distance."""
            ans, prev = 0, float('-inf') # where previous ball is put
            for x in position:
                if x - prev >= d: 
                    ans += 1
                    if ans == m: return True
                    prev = x
            return False 
        
		# "last True" binary search (in contrast to "first True" binary search)
        lo, hi = 1, position[-1] - position[0]
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            if fn(mid): lo = mid
            else: hi = mid - 1
        return lo