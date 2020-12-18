from typing import DefaultDict
"""
3. Longest Substring Without Repeating Characters
*Medium*
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = dict()
        cursor_start = 0
        cursor_len = 0
        longest = 0
        for i, letter in enumerate(s):
            if letter in sub and sub[letter] >= cursor_start:
                cursor_start = sub[letter] + 1
                cursor_len = i - sub[letter]
                sub[letter] = i
            else:
                sub[letter] = i
                cursor_len += 1
                if cursor_len > longest:
                    longest = cursor_len

        return longest

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        long_str = ''
        len_val = 0
        for i in range(len(s)):
            if s[i] not in long_str:
                long_str += s[i]
            else:
                ref_ind = long_str.find(s[i])
                len_val = max(len_val, len(long_str))
                long_str = long_str[ref_ind+1:]+s[i]
        return max(len_val, len(long_str))
