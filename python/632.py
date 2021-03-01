"""
632. Smallest Range Covering Elements from K Lists
Hard

You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
Example 3:

Input: nums = [[10,10],[11,11]]
Output: [10,11]
Example 4:

Input: nums = [[10],[11]]
Output: [10,11]
Example 5:

Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
Output: [1,7]
 

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.
"""

from itertools import zip_longest
from collections import defaultdict
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        table=defaultdict(list)
        for i in zip_longest(*nums):
            for j,k in enumerate(i):
                if k==None:
                    continue
                table[k].append(j)
        res=[i for i,j in sorted(table.items(), key=lambda x: x[0])]
        check=set()
        table2=defaultdict(int)
        length=len(nums)
        ans=None
        left=right=0
        while right<len(res):
            while right<len(res) and len(check)<length:
                for i in table[res[right]]:
                    table2[i]+=1
                    if table2[i]>0:
                        check.add(i)
                right+=1
            while left<right and len(check)==length:
                if ans==None or (ans[1]-ans[0])>(res[right-1]-res[left]):
                    ans=[res[left], res[right-1]]
                for i in table[res[left]]:
                    table2[i]-=1
                    if table2[i]<=0:
                        check.remove(i)
                left+=1
        return ans