"""
209. Minimum Size Subarray Sum
Medium

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""
from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        res = float('inf')
        for right in range(len(nums)):
            # move the right side of the window
            curr_sum += nums[right]
            #  meet the conditions
            while curr_sum >= s:
                # update res
                res = min(res, right - left + 1)
                # shrink the left side of the window
                curr_sum -= nums[left]
                left += 1
        return 0 if res == float('inf') else res
    
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        if not nums or sum(nums) < target:
            return 0

        result = len(nums)
        l = 0
        cur_val = 0
        
        for r in range(len(nums)):
            cur_val += nums[r]
            while l < r:
                if cur_val - nums[l] >= target:
                    cur_val -= nums[l]
                    l += 1
                    
                else:
                    break
            if cur_val >= target:
                result = min(r - l + 1, result)
            
        return result