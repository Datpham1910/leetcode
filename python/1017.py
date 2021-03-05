"""
1017. Convert to Base -2
Medium 

Example 1:

Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
Example 2:

Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
Example 3:

Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4
 

Note:

0 <= N <= 10^9
"""

class Solution:
    def baseNeg2(self, N: int) -> str:

        """
        If we have base 2, then we start dividing by 2 until the number becomes 0. At every step the reminder will be the next digit in the number (from low to high). So the logic would be like:

        3 base 2:

        1,1 = divmod(3,2), so the new number is 1 and the lowes digit is 1: "...1"
        0,1 = divmod(1,2), the new number is 0(we are done!), the next digit is 1: "11"
        (just as a reference: The divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder. )

        But for the negative base it looks a bit different:

        -2, -1 = divmod(3, -2). This is the key part. The reminder is supposed to be our highest digit. But it can be only 0 or 1 ( or generally: 0 <= digits <= ((abs(base) -1) ). So when we divide by -2, we can get 3 possible values: 0, 1 and -1. The first 2 scenarios are straightforward and they are the same as with base=2. But how should we hand -1? Basically how can we convert that '-1' into a non-negative digit? Ok, so let's see:
        -2, -1 = divmod(3, -2) - that means 3 = (-2) x (-2 <--- This is quotient ) + (-1 <--- This is reminder)

        Now let's add 0=base - base = -2 + 2:

        3 = (-2) x (-2 ) + (-1) = (-2) x (-2 ) + (-1) -2 +2 = (-2)x(-2) -2 -1 + 2 = (-2)x(-2+1 <--- New quotient ) +1 <--- New reminder

        This is the key transformation. basically we are saying that 3 divided by (-2) can be presented either as:

        -2 with a reminder of -1

        or:

        -2+1 with a reminder of 1

        Does that make sense to you? basically we can replace reminder -1 with -1 - (-2) = 1 if we add 1 to the quotient. In case of base = -2, a simple way to implement that logic would be just to use r=abs(r). A more universal (but longer way) would be r = (r - BASE if r<0 else r))

        If yes, then now we have the code above. we need to check just 3 conditions:

        Is the current number 0 (as part of the loop)?
        is the reminder < 0?
        this is specific to python. Python doesn't have a do ... while loop, only while ... So if our input value is 0, we can't tell python to run one cycle and generate the "0" output. as a result we need an extra if to handle the 0 input. In this case we use an implicit condition check as return max(ans,"0") but it can be written explicitely as return ans if ans else "0"
        Ok, so now we just need to arrange our 1 loop and 2 if statements.

        Also, one tip. In most solutions you'll see something like result.append(current_digit), then result.reversed() and then ''.join(result) - a sequence of those 3 operations in some form. Each step looks clear and logical, but if you think about it, what if we use ans = str(abs(r)) + ans instead ... ? then you can combine all 3 steps into 1. you're forming the output string in a proper order right away in one line. Nice, right?

        Another tip ... while N!=0: can be replaced with while N: - that will work and it's a shorter code. However, it will require python to do extra conversion, so generally speaking N!=0 should be faster. Since we repeat that check many times in the loop - this is where every improvement count and we should stick with explicit !=0.

        Final tip. You may see if N==0: return "0" at the very top in some solutions. While the explanation makes sense (let's fail quickly), if you compare it against having a single return statement at the very end ... what do you think makes it easier to follow the flow? Or which approach would make it easier to verify or modify your return value?

        Ok, so how can we modify this solution for any base?

        let's rewrite to explicitly state our base:
        """
        BASE,ans = -2,''
        while N!=0:
            N, r = divmod(N, BASE)
            if r<0:
                N,r = N+1, r-BASE
            ans = str(r) + ans
        return max(ans,"0")