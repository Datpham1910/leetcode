"""
* 319. Bulb Switcher
* Medium

There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

 

Example 1:


Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 1
 

Constraints:

0 <= n <= 109
"""
import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        
        # consider the number of divisors of a given number
        
        # 0 is divisible by everything
        
        # nth round, only toggle the n-1th bulb (0-based)
        
        # you will sweep by every number (all of its divisors)
        
        # maybe you should ignore the 1st bulb
        
        # its the 0th bulb anyways
        
        # divide by 1
        # divide by 2
        # divide by 3
        # divide by n
        
        # a divisor below the square root always has a complement above the square root
        
        # is the divisor a perfect square?
        
        # means you'll switch a bulb an even number of times unless it has a square root
        
        # 
        # 0th nulb is always on because its degenerate
        
        # yeah, they just did something random with 0th bulb
        
        # how many numbers are perfect squares?
        
        # [1,n]
        
        # 1 is a perfect square, yup
        
        return math.isqrt(n)