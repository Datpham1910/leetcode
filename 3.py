from typing import DefaultDict


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
        if len(s)<2:
            return len(s)        
        long_str=''
        len_val=0
        for i in range(len(s)):
            if s[i] not in long_str:
                long_str+=s[i]
            else:
                ref_ind=long_str.find(s[i])
                len_val=max(len_val,len(long_str))
                long_str=long_str[ref_ind+1:]+s[i]
        return max(len_val,len(long_str))