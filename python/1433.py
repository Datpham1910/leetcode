"""
1433. Check If a String Can Break Another String
Medium

Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa. In other words s2 can break s1 or vice-versa.

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.

Example 1:

Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".
Example 2:

Input: s1 = "abe", s2 = "acd"
Output: false 
Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.
Example 3:

Input: s1 = "leetcodee", s2 = "interview"
Output: true
 

Constraints:

s1.length == n
s2.length == n
1 <= n <= 10^5
All strings consist of lowercase English letters.
"""

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        l1 = []
        l2 = []
        n = len(s1)
        index = 0
        while index < n:
            l1.append(s1[index])
            l2.append(s2[index])
            index += 1
        l1.sort()
        l2.sort()
        l1_check = []
        l2_check = []
        for index in range(n):
            if l1[index] == l2[index]:
                l1_check.append(1)
                l2_check.append(1)
            elif l1[index] > l2[index]:
                l1_check.append(1)
                l2_check.append(0)
            else:
                l1_check.append(0)
                l2_check.append(1)

        if sum(l1_check) == n or sum(l2_check) == n:
            return True
        return False

    def checkIfCanBreak1(self, s1: str, s2: str) -> bool:
        import string
        numer1 = True
        numer2 = True
        count = 0
        for ch in string.ascii_lowercase:
            count += s1.count(ch) - s2.count(ch)
            if count < 0:
                numer1 = False
            if count > 0:
                numer2 = False
        return numer1 or numer2