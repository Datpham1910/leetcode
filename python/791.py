"""
* 791. Custom Sort String
* Medium

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.


Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
"""


from typing import Counter


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        d = {}
        for k, v in enumerate(S):  # {c: 0, b: 1, a: 2}
            d[v] = k
        d_opposite = {}

        for k, v in d.items():  # {0: c, 1: b, 2: a}
            d_opposite[v] = k
        T_nums = []
        for ch in T:
            if ch in d:
                T_nums.append(d[ch])
        T_nums.sort()
        res = []
        for num in T_nums:
            res.append(d_opposite[num])
        if len(res) != len(T):
            for ch in T:
                if ch not in d:
                    res.append(ch)
        return ''.join(res)

    def customSortString1(self, S: str, T: str) -> str:
        count = Counter(T)
        answer = ''
        for s in S:
            answer += s * count[s]
            count[s] = 0
        for c in count:
            answer += c * count[c]
        return answer

    def customSortString2(self, S: str, T: str) -> str:
        res = T
        for char in S[-1::-1]:
            if char in T:
                res = char * T.count(char) + ''.join(res.split(char))
        return res


if __name__ == "__main__":
    print(Solution().customSortString(S="cba", T="abcd"))
