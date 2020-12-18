class Solution:
    def reverse(self, x: int) -> int:
        f = x < 0
        x = str(abs(x))
        x = list(x)
        x.reverse()
        x = int("".join(x))
        x = -1*f*x + (not f)*x
        if abs(x) > 2**31:
            return 0
        return x
    def reverse2(self, x: int) -> int:
        reverse = 0
        sign = 1
        if x < 0:
            sign = -1
            x = x * -1
        while x > 0:
            rem = x % 10
            reverse = reverse*10 + rem
            x = x //10
        if not -2**31 < reverse < 2**31 - 1:
            return 0
        return sign * reverse