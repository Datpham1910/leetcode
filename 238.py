"""
Medium
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        r = 1
        j = len(nums) - 1
        i = 1
        while i < len(nums):
            value = nums[i -1] * output[i - 1]
            output.append(value)
            i += 1
        while j >= 0:
            output[j] = output[j] * r
            r = r * nums[j]
            j -= 1
        return output

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]
        for i in range(n-1):
            res.append(res[-1] * nums[i])
        temp = 1
        for i in range(n-1, -1, -1):
            res[i] *= temp
            temp *= nums[i]
        return res
print(Solution().productExceptSelf([1,2,3,4]))