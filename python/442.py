"""
442. Find All Duplicates in an Array
Medium
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""
from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                output.append(index + 1)
            nums[index] = -nums[index]
        return output

    def findDuplicates2(self, nums: List[int]) -> List[int]:
        s = set()
        ans = []
        for n in nums:
            if n in s:
                ans.append(n)
            s.add(n)
        return ans
print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))