from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Time complexity: O(N^2)
        # Extra space complexity: O(N)

    # def twoSum2(self, nums: List[int], target: int) -> List[int]:
    #     i = 0
    #     j = 0
    #     aSum = 1
    #     cnt = 0
    #     while i < len(nums):
    #         if aSum + nums[i] < target:
    #             aSum += nums[i]
    #             i += 1
    #         elif aSum + nums[i] > target:
    #             aSum -= nums[j]
    #             j += 1
    #         else:
    #             cnt += 1
    #             aSum += nums[i]
    #             i += 1
    #     return [cnt, cnt + 1]
    #     # Time Complexity: ___
    #     # Extra Space Complexity: ___
print(Solution().twoSum([3,2,4], 6))