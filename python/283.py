"""
283. Move Zeroes
Easy

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        index = 0
        length = len(nums)
        while count < length:
            if nums[count] != 0:
                temp = nums[count]
                nums[count] = nums[index]
                nums[index] = temp
                index += 1
            count += 1
        return nums

    def moveZeroes1(self, nums: List[int]) -> None:
        a = 0
        for i in nums:
            if i == 0:
                a = a + 1
        for j in range(a):
            nums.remove(0)
            nums.append(0)
            
        print(nums)


if __name__ == "__main__":
    print(Solution().moveZeroes([0, 1, 0, 3, 12]))
