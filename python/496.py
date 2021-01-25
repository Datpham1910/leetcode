"""
496. Next Greater Element I
Easy

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = dict()
        stack = nums2[0:1]

        for num in nums2[1:]:
            while stack and stack[-1] < num:
                hash_map[stack.pop()] = num
            stack.append(num)
        return [hash_map.get(num, -1) for num in nums1]

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:

        table = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                table[stack.pop()] = num
            stack.append(num)

        return [table[num] if num in table else -1 for num in nums1]

    def nextGreaterElement3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        aDict = {el: i for i, el in enumerate(nums1)}
        stack = []
        finals = [-1 for _ in range(len(nums1))]
        for x in nums2:
            if not stack:
                stack.append(x)
            else:
                while stack and x > stack[-1]:
                    if stack[-1] in aDict:
                        finals[aDict[stack[-1]]] = x
                    stack.pop()
                stack.append(x)
        return finals


if __name__ == "__main__":
    print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))
