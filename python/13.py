class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total, prev, curr = 0,0,0
        for i in range(len(s)):
            curr = roman_dict[s[i]]
            if curr > prev:
                total = total + curr - 2 * prev
            else:
                total += curr

            prev = curr
        return total

print(Solution().romanToInt('MCMXCIV'))