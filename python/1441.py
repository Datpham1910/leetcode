"""
1441. Build an Array With Stack Operations
Easy

Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
Return the operations to build the target array. You are guaranteed that the answer is unique.

Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: 
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]
Example 2:

Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]
Example 3:

Input: target = [1,2], n = 4
Output: ["Push","Push"]
Explanation: You only need to read the first 2 numbers and stop.
Example 4:

Input: target = [2,3,4], n = 4
Output: ["Push","Pop","Push","Push","Push"]
 

Constraints:

1 <= target.length <= 100
1 <= target[i] <= n
1 <= n <= 100
target is strictly increasing.
"""
from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """
        Time Complexity: O(N)
        Runtime: Faster than 99% (as of May 11th, 2020)
        Memory Usage: Less than 100%
        Explanation:
        Step 1: Create an empty list res to store the result.
        Step 2: Add the elements of the input array target to a set to improve lookup performance.
        Step 3: Iterate through the integers of target and add "Push" to the res list for each integer in range(1, target[-1] + 1). Then, add "Pop" if the integer is not in the set.
        Step 4: Return the result.
        Note: The n parameter is not used in this approach.
        """
        res = []
        s = set(target)
        for i in range(1, target[-1] + 1):
            res.append("Push")
            if i not in s:
                res.append("Pop")
        return res