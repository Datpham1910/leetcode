from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        r = 0
        v = list()
        for i in range(len(nums)):
            r += nums[i]
            v.append(r)

        return v

print(Solution().runningSum([1,2,3,4]))