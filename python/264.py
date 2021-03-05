"""
264. Ugly Number II
Medium

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        Let us solve this problem for general case: that is not only for 2,3,5 divisors, but for any of them and any number of them. factors = [2,3,5] and k=3 in our case.
Let Numbers be an array, where we keep all our ugly numbers. Also, note, that any ugly number is some other ugly number, multiplied by 2, 3 or 5. So, let starts be the indexes of ugly numbers, that when multiplied by 2, 3 or 5 respectively, produces the smallest ugly number that is larger than the current overall maximum ugly number.. Let us do several first steps to understand it better:

starts = [0,0,0] for numbers 2,3,5, so new_num = min(1*2,1*3,1*5) = 2, and now starts = [1,0,0], Numbers = [1,2].
starts = [1,0,0], so new_num = min(2*2,1*3,1*5) = 3, and now starts = [1,1,0], Numbers = [1,2,3].
starts = [1,1,0], so new_num = min(2*2,2*3,1*5) = 4, so now starts = [2,1,0], Numbers = [1,2,3,4].
starts = [2,1,0], so new_num = min(3*2,2*3,1*5) = 5, so now starts = [2,1,1], Numbers = [1,2,3,4,5].
starts = [2,1,1], so new_num = min(3*2,2*3,2*5) = 6, so let us be carefull in this case: we need to increase two numbers from start, because our new number 6 can be divided both by 2 and 3, so now starts = [3,2,1], Numbers = [1,2,3,4,5,6].
starts = [3,2,1], so new_num = min(4*2,3*3,2*5) = 8, so now starts = [4,2,1], Numbers = [1,2,3,4,5,6,8]
starts = [4,2,1], so new_num = min(5*2,3*3,2*5) = 9, so now starts = [4,3,1], Numbers = [1,2,3,4,5,6,8,9].
starts = [4,3,1], so new_num = min(5*2,4*3,2*5) = 10, so we need to update two elements from starts and now starts = [5,3,2], Numbers = [1,2,3,4,5,6,8,9,10]
starts = [5,3,2], so new_num = min(6*2,4*3,3*5) = 12, we again need to update two elements from starts, and now starts = [6,4,2], Numbers = [1,2,3,4,5,6,8,9,10,12].
starts = [6,4,2], so new_num = min(8*2,5*3,3*5) = 15, we again need to update two elements from starts, and now starts = [6,5,3], Numbers = [1,2,3,4,5,6,8,9,10,12,15].
Complexity: time complexity is O(n) to find ugly number with number n, because on each step we check 3 possible candidates. Space complexity is O(n) as well. Note, that it can be easily generalized for different amount of divisors with time complexity O(nk), where k is total number of divisors.
        """
        factors, k = [2,3,5], 3
        starts, Numbers = [0] * k, [1]
        for i in range(n-1):
            candidates = [factors[i]*Numbers[starts[i]] for i in range(k)]
            new_num = min(candidates)
            Numbers.append(new_num)
            starts = [starts[i] + (candidates[i] == new_num) for i in range(k)]
        return Numbers[-1]

class Ugly:
    def __init__(self):
        self.nums = [1]
        
        idx2 = 0
        idx3 = 0
        idx5 = 0
        for i in range(1, 1690):
            ugly = min(self.nums[idx2] * 2, self.nums[idx3] * 3, self.nums[idx5] * 5)
            
            self.nums.append(ugly)
            if ugly == self.nums[idx2] * 2:
                idx2 += 1
            if ugly == self.nums[idx3] * 3:
                idx3 += 1
            if ugly == self.nums[idx5] * 5:
                idx5 += 1
class Solution:
    u = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n-1]