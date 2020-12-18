from typing import List
"""
* 845. Longest Mountain in Array *
* Medium *

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
 

Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
"""


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i = result = 0

        while i < len(arr):
            base = i

            while i+1 < len(arr) and arr[i] < arr[i+1]:
                i += 1

            if i == base:
                i += 1
                continue

            # walk down
            summit = i

            while i+1 < len(arr) and arr[i] > arr[i+1]:
                i += 1

            # same i (cannot have 2 summit)
            if i == summit:
                i += 1
                continue

            result = max(result, i - base + 1)
        # T:O(n)
        # S:O(1)
        return result

    def longestMountain2(self, arr: List[int]) -> int:
        res = up = down = 0
        for i in range(1, len(arr)):
            if down and arr[i - 1] < arr[i] or arr[i - 1] == arr[i]:
                up = down = 0
            print('up {}, down {}, res {}'.format(up, down, res))
            up += arr[i - 1] < arr[i]
            down += arr[i - 1] > arr[i]
            print('after += : up {}, down {}, res {}'.format(up, down, res))
            if up and down:
                res = max(res, up + down + 1)
            print('end of loop: up {}, down {}, res {}'.format(up, down, res))
            print('---------')
        # T:O(n)
        # S:O(1)
        return res

if __name__ == "__main__":
    Solution().longestMountain2([2,1,4,7,3,2,5])