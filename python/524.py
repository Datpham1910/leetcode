"""
524. Longest Word in Dictionary through Deleting
Medium

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""
from typing import List
class Solution:
    def check(self, s,s1):
        i=0
        j=0
        while(i<len(s) and j<len(s1)):
            if s[i]==s1[j]:
                i=i+1
                j=j+1
                continue
            i=i+1
        return j==len(s1)
    
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res=""
        for word in d:
            if self.check(s,word) and (len(res)<len(word) or (len(res)==len(word) and res>word)):
                res=word
        return res

    def findLongestWord1(self, s: str, d: List[str]) -> str:        
        d.sort(key = lambda x:(-len(x), x))
        
        for word in d:
            start = -1
            for char in word:
                start = s.find(char, start+1)
                if start == -1:
                    break
              
            if start != -1:
                return word
        
        return ""
if __name__ == "__main__":
    print(Solution().findLongestWord(s = "abpcplea", d = ["ale","apple","monkey","plea"]))
    print(Solution().findLongestWord(s = "abpcplea", d = ["a","b","c"]))