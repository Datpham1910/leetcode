"""
767. Reorganize String
Medium

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
import heapq
import collections


class Solution(object):
    def reorganizeString(self, S):
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            #This code turns out to be superfluous, but explains what is happening
            #if not ans or ch1 != ans[-1]:
            #    ans.extend([ch1, ch2])
            #else:
            #    ans.extend([ch2, ch1])
            ans.extend([ch1, ch2])
            if nct1 + 1:
                heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1:
                heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')

    def reorganizeString1(self, S: str) -> str:
        dct = collections.Counter(S)
        max_elem = dct.most_common(1)[0]
        if (len(S) % 2 == 0 and max_elem[1] > len(S)/2) or max_elem[1] > (len(S)//2 + 1):
            return ""
        ret_lst = ["" for i in range(max_elem[1])]
        ind = 0
        for k in dct:
            if k == max_elem[0]:
                continue
            v = dct[k]
            for i in range(v):
                ret_lst[ind % max_elem[1]] += k
                ind += 1
        ret = ""
        for s in ret_lst:
            ret += max_elem[0] + s
        return ret


if __name__ == "__main__":
    Solution().reorganizeString("aab")
