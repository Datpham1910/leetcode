"""
18. 4Sum
Medium

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.


Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
 

Constraints:

0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

"""
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums: return [] 
        nums.sort()
        n=len(nums)
        nums_dict={i:j for j,i in enumerate(nums)}
        seen=set()
        M=nums[-1]
        for i in range(n-3):
            a=nums[i]
            if  4*a > target: break
            if a+3*M < target: continue
            for j in range(i+1, n-2):
                b=nums[j]
                if a+3*b > target: break
                if a+b+2*M < target: continue
                for k in range(j+1,n-1):
                    c=nums[k]
                    d=target-(a+b+c)
                    if d>M: continue
                    if d<c: break
                    if d in nums_dict and nums_dict[d]>k: seen.add((a,b,c,d))
        return list(seen)


if __name__ == "__main__":
    print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))