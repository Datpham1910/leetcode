"""
459. Repeated Substring Pattern
Easy

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000. 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(1, (l//2)+1):
            if l % i == 0 and s[0:i]*(l//i) == s:
                return True
        return False

    def repeatedSubstringPattern1(self, s: str) -> bool:
        l = len(s)
        if l % 2 == 1:
            for i in range(1, (l//2)+1, 2):
                kp = 0
                if l % i == 0:
                    to = s[0:i]
                    for j in range(0, l, i):
                        if to != s[j:j+i]:
                            kp = 1
                    if kp == 0:
                        return True
            return False
        else:
            for i in range(1, (l//2)+1):
                kp = 0
                if l % i == 0:
                    to = s[0:i]
                    for j in range(0, l, i):
                        if to != s[j:j+i]:
                            kp = 1
                    if kp == 0:
                        return True
            return False


if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern("abcabcabcabc"))
