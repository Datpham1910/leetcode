"""
1370. Increasing Decreasing String
Easy

Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
Example 3:

Input: s = "leetcode"
Output: "cdelotee"
Example 4:

Input: s = "ggggggg"
Output: "ggggggg"
Example 5:

Input: s = "spo"
Output: "ops"
 

Constraints:

1 <= s.length <= 500
s contains only lower-case English letters.
"""

class Solution:
    def sortString(self, s: str) -> str:
		#result string
        result:str = ""
        #Table of frequencies
        freqTable = []
        '''
        create sorted set in order to pick unique character in ascending order -> step 1-2,
        then do it again in descending order -> step 4-5
        had to use "dict.fromkeys()" instead of set() to preserve the order of elements
        '''
        sortedSet = sorted(list(dict.fromkeys(s)))
        #counting frequencies
        for x in sortedSet:
            freqTable.append(s.count(x))
        
        #while there are some unused characters with frequency > 0 -> step 7
        while(sum(freqTable) != 0):
            #appending characters in ascending order -> step 1-2-3
            for i in range(len(sortedSet)):
				#if frequency of particular character is > 0 we can add it to our result string
                if freqTable[i] > 0:
                    result += sortedSet[i]
					#Decreasing frequency of a character
                    freqTable[i] -= 1
            #appending characters in descending order -> step 4-5-6
            for i in range(len(sortedSet)-1, -1, -1):
                if freqTable[i] > 0:
                    result += sortedSet[i]
                    freqTable[i] -= 1
        return result