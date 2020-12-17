"""
1295. Find Numbers with Even Number of Digits
Easy
Given an array nums of integers, return how many of them contain an even number of digits.
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([int(log10(num)) %2 for num in nums])
        
    def findNumbers2(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count += 1
        return count