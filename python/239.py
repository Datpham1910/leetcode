"""
239. Sliding Window Maximum
Hard

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
from typing import List


from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
# Checking for base case
        if not nums:
            return []
        if k == 0:
            return nums
# Defining Deque and result list
        deq = deque()
        result = []
        
# First traversing through K in the nums and only adding maximum value's index to the deque.
# Note: We are olny storing the index and not the value.
# Now, Comparing the new value in the nums with the last index value from deque,
# and if new valus is less, we don't need it

        for i in range(k):
            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break

            deq.append(i)
            
# Here we will have deque with index of maximum element for the first subsequence of length k.
	
# Now we will traverse from k to the end of array and do 4 things
# 1. Appending left most indexed value to the result
# 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
# 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it
# 4. Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)
 
        for i in range(k, len(nums)):
            result.append(nums[deq[0]])
            
            if deq[0] < i - k + 1:
                deq.popleft()
            
            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            
            deq.append(i)
        
#Adding the maximum for last subsequence
        result.append(nums[deq[0]])
        
        return result