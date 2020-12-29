"""
50. Pow(x, n)
Medium

Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            return self.cPow(1/x, abs(n))
        else:
            return self.cPow(x, n)

    def cPow(self, x, n):
        if n == 0:
            return 1

        a = self.cPow(x, n // 2)
        if (n % 2 == 0):
            return a**2
        else:
            return x*(a**2)

    def myPow1(self, x: float, n: int) -> float:
        absn = abs(n)
        neg = False
        if n < 0:
            neg = True

        ans = 1.0
        while absn != 0:
            if absn % 2 == 1:
                ans = ans * x  # check if bit is set then x will be multiplied to answer. ( x is updating each time )
            x = x*x
            absn = int(absn / 2)  # this operation will be done logn times

        return ans if not neg else 1/ans

    def myPow2(self, x: float, n: int) -> float:
        
        if n==0:
            return 1
        
        if x==0:
            return 0
        
        if n<0:
            n = -n
            x = 1.0/x
        
        res = 1
        current_product = x
        
        while n>0:
            if n%2==1:
                res = res*current_product
            current_product = current_product * current_product
            n = n//2
        
        return res

if __name__ == "__main__":
    print(Solution().myPow1(2.00000, 10))
