from typing import List    

class Solution:
    def advancedMod(self, a,b,c):
        res = 1
        a = a % c
        while b > 0:
            if b % 2 == 1:
                res = (res * a) % c
            b = b // 2
            a = (a * a) % c
        return res
    
    def superPow(self, a: int, b: List[int]) -> int:
        st = ''
        for item in b:
            st += str(item)
        st = int(st)
        return self.advancedMod(a, st, 1337)


    def superPow1(self, a: int, b: List[int]) -> int:
        c = ""
        for n in b:
            c+=str(n)
        return (a%1337) ** (int(c)%1140) % 1337