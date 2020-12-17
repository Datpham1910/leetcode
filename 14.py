from typing import List


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        pref = strs[0]
        plen = len(pref)
        for s in strs[1:]:
            while pref != s[0:plen]:
                pref = pref[0:(plen -1)]
                plen -= 1
                if plen == 0:
                    return ""

        return pref

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        result = ''   
        if not strs:
            return ''
        else:
            for i in zip(*strs):
                if len(set(i)) == 1:
                    result += i[0]
                else:
                    break
        return result
print(Solution().longestCommonPrefix2(["flower","flow","flight"]))