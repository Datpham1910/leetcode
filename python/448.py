"""
448. Find All Numbers Disappeared in an Array
Easy

Share
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        The idea is to use the original array to keep track of the numbers visited. Since all the numbers are positive intergers, for every number visited we mark the presence of that number by negating the number at the index equal to the current number. Since Python follows 0-indexing, the index we mark is actually number - 1. If the number at that index is already negated we do nothing. In the end, we just return the indices (index + 1 for the number) where there are still postive numbers.
        Still confused?? I hope the following example will make it clearer:
        Let nums = [4, 3, 2, 7, 8, 2, 3, 1]. Now let's iterate through the array nums.

        At iter = 0,
        current number: |4| (|.| here refers to taking the absolute value)
        number at index = 3 (current number - 1): 7
        After negation: nums = [4, 3, 2, -7, 8, 2, 3, 1]

        At iter = 1
        current number: |3|
        number at index = 2: 2
        After negation: nums = [4, 3, -2, -7, 8, 2, 3, 1]

        At iter = 2
        current number: |-2|
        number at index = 1: 3
        After negation: nums = [4, -3, -2, -7, 8, 2, 3, 1]

        At iter = 3
        current number: |-7|
        number at index = 6: 3
        After negation: nums = [4, -3, -2, -7, 8, 2, -3, 1]

        At iter = 4
        current number: |8|
        number at index = 7: 1
        After negation: nums = [4, -3, -2, -7, 8, 2, -3, -1]

        At iter = 5
        current number: |2|
        number at index = 1: -3
        Array stays unchanged: nums = [4, -3, -2, -7, 8, 2, -3, -1]

        At iter = 6
        current number: |-3|
        number at index = 2: -2
        Array stays unchanged: nums = [4, -3, -2, -7, 8, 2, -3, -1]

        At iter = 7
        current number: |-1|
        number at index = 0: 4
        After negation: nums = [-4, -3, -2, -7, 8, 2, -3, -1]

        Now the indices at which there are still positive numbers are the numbers (index+1) that weren't present in the array.
        """
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)

        return res

    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            while nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
            
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(i+1)

        return res


if __name__ == "__main__":
    print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print(Solution().findDisappearedNumbers1([4, 3, 2, 7, 8, 2, 3, 1]))
