"""
* 8. String to Integer (atoi) * 
* Medium *

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, 231 − 1 or −231 is returned.
 

Example 1:

Input: str = "42"
Output: 42
Example 2:

Input: str = "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: str = "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: str = "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: str = "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned.
 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits, ' ', '+', '-' and '.'.
"""
import re

class Solution:
    # def myAtoi(self, s: str) -> int:
    #     MAX_INT = 2 ** 31 - 1
    #     MIN_INT = -2 ** 31
    #     #2147483648
    #     #21474836460
    #     i, res, negative = 0, 0, 1

    #     # while space
    #     while i < len(s) and s[i] == ' ':
    #         i += 1
    #     if i < len(s) and s[i] == '-':
    #         i += 1
    #         negative = -1
    #     elif i < len(s) and s[i] == '+':
    #         i += 1

    #     check = set('0123456789')
    #     while i < len(s) and s[i] in check:
    #         print(s[i], negative, res)
    #         if 10 > int(s[i]) > 1:
    #             return MAX_INT if negative == 1 else MIN_INT

    #         if res > MAX_INT / 10 or (res == MAX_INT / 10 and int(s[i]) > 7):
    #             return MAX_INT if negative == 1 else MIN_INT
    #         res = res * 10 + int(s[i])
    #         i += 1
    #     return res * negative

        
    def myAtoi2(self, s: str) -> int:
        pat = "^((?:-|\+)?(?:[0-9])*(?:\.)?(?:[0-9])+)(?:[\+\.\- \w])*$"
        m = re.match(pat, s.strip())
        if m != None:
            match = m.groups()[0]
            if "." in match:
                number = int(float(match))
            else:
                number = int(match)
            
            if number >= (max_int := 2**31-1):
                return max_int
            elif number <= (min_int := -2**31):
                return min_int
            else:
                return number
        else:
            return 0

if __name__ == "__main__":
    res = Solution().myAtoi2("4193 with words")
    print(res)
