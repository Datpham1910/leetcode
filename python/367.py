"""
367. Valid Perfect Square
Easy

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        Newton's Method, also known as the Babylonian Method, can be used to quickly approximate the square root (it converges quadratically, 
        
        so the number of correct digits doubles each iteration).

        After getting a good approximation, we can round our approximation to the nearest integer and check whether that squares to give our original number.

        Since it converges so quickly, we can be safe to run 20 iterations to pass all test cases.

        class Solution:
        """
        x = 1 ## Start at 1
        
        ## Apply Newton's Method for 20 iterations:
        for _ in range(20):
            x = 0.5 * (x + (num / x))
        
        ## Check if the result squares to give num
        if pow(round(x), 2) == num:
            return True
        
        return False