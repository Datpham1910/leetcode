"""
313. Super Ugly Number
Medium

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
""" 
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """
        First, let’s determine the route to solve this problem.

        We need to find Nth number. So, what we need to do is:

        Find the 1st smallest number
        Find the 2nd smallest number
        Find the 3rd smallest number
        .....
        Finally, we find the Nth number
        This is actually Dynamic Programming.

        Take primes = [2, 7, 13, 19], n = 12 as an example:

        n = 1, of course, we return 1
        n = 2, we already have [1], so, we do the calculation: 2 x 1, 7 x 1, 13 x 1, 19 x 1,
        we got [2, 7, 13, 19], the smallest number is 2, so, we return 2.
        n = 3, we already have [1, 2]. Last time, we chose 2 from [2, 7, 13, 19], so, we do the calculation: 2 x 2 to replace the 2. So, we got [4, 7, 13, 19, the smallest number is 4, so, we return 4.
        Hold on ! Hold on ! Why we compute 2 x 2 ????, not 2 x 3 or 7 x 2 or anything else ?

        Let us figure out this problem !!!


        What we need to do at each step is to find the next smallest number based on the numbers we have found.
        We use Multiplication to produce the new number, so, what is the strategy for producing as small a number as possible?
        We choose the smallest numbers to multiply !!!


        So, at step 3, we already have [1, 2], the primes are [2, 7, 13, 19]. Since we have compute 1 x primes, this time, we just need to compute 2 x primes.
        But do we really need to do the calculation: 7 x 2, 13 x 2, 19 x 2 ???
        No! We have not chose 7 x 1, 13 x 1, 19 x 1 yet !!! There is no possibility that we will choose the smallest number from [ 7 x 2, 13 x 2, 19 x 2]. So, we just need to compute 2 x 2 to get [4, 7, 13, 19].

        Things get easy, right ???

        Let us keep on:

        n = 4
        dp = [1, 2, 4] # the numbers we have found

        # the index of the factors we choose from dp to multiply primes
        # e.g if we choose nth number as ugly number, then, index[n-1] += 1
        # so index will move to the right, which means we will replace the number
        index = [2, 0, 0, 0]

        # ** number ** means we will choose this number
        ugly_nums = [ 2 x dp[index[0]], **7 x dp[index[1]]**, 13 x dp[index[2]], 19 x dp[index[3]] ]
        n = 5
        dp = [1, 2, 4, 7]
        index  = [2, 1, 0, 0]
        ugly_nums = [ **2 x 4**, 7 x 2, 13 x 1, 19 x 1 ]
        n = 6
        dp = [1, 2, 4, 7, 8]
        index  = [3, 1, 0, 0]
        ugly_nums = [ 2 x 7, 7 x 2, **13 x 1**, 19 x 1 ]
        n = 7
        dp = [1, 2, 4, 7, 8]
        index  = [3, 1, 1, 0]
        ugly_nums = [ **2 x 7**, **7 x 2**, 13 x 2, 19 x 1 ]
        If we have some same numbers, we choose only one value, but we will replace all of them at next step.
        8. n = 8

        dp = [1, 2, 4, 7, 8]
        index  = [4, 2, 1, 0]
        ugly_nums = [ **2 x 8**, 7 x 4, 13 x 2, 19 x 1 ]
        ......
        Finally, we will got the answers.
        As you can see, we need to keep:

        The ugly number we found last time
        All the ugly numbers we have found
        The indexes in dp to multiply the prime number.
        """
        size = len(primes)
        ugly, dp, index, ugly_nums = 1, [1], [0] * size, [1] * size
        for i in range(1, n):
            # compute possibly ugly numbers and update index
            for j in range(0, size):
                if ugly_nums[j] == ugly:
                    ugly_nums[j] = dp[index[j]] * primes[j]
                    index[j] += 1
            # get the minimum
            ugly = min(ugly_nums)
            dp.append(ugly)
        return dp[-1]