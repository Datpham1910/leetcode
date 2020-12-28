"""
443. String Compression
Medium

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
Example 4:

Input: chars = ["a","a","a","b","b","a","a"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","3","b","2","a","2"].
Explanation: The groups are "aaa", "bb", and "aa". This compresses to "a3b2a2". Note that each group is independent even if two groups have the same character.
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lower-case English letter, upper-case English letter, digit, or symbol.
"""
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        cur = ''
        l, counter = 0, 1
        
        for i in chars:
            if i != cur:
                if counter != 1:
                    for j in str(counter):
                        chars[l] = j
                        l+=1
                chars[l] = i
                l+=1
                cur=i
                counter=1
            else:
                counter+=1
        
        if counter != 1:
            for j in str(counter):
                chars[l] = j
                l+=1
        
        while len(chars) > l:
            chars.pop()
        
        return chars

    def compress1(self, chars: List[str]) -> int:
        #od = OrderedDict(Counter(chars))
        #print(od)
        #for key in od.keys():
        #    pass
        n = len(chars) #length of the chars list
        
        #if only 1 char in the list then return it
        #As 1 <= chars.length <= 2000, we don't need to think of empty chars list
        if(n == 1):
            return 0
        #Otherwise, we will go for checking each character and whether it is same as the previous one
        #if same as previous, we increase the count. Otherwise we extend the out_list with the char and 
        #with count value when applicable (when count >1)
        out_list = []
        prev = chars[0] #start prev with the first element
        count = 1 #so starting count from 1
        for i in range(1,n):
            current = chars[i] #setting the current character we are examining
            if (current == prev): #if current = prev count increases
                count +=1
            else:                 #otherwise prepare for putting that char in the out_list
                if(count == 1):
                    out_list.extend([prev])
                else:
                    out_list.extend([prev, *list(str(count))])
                count = 1 #count set to starting count again when current != prev
            prev = current
            if(i == n-1):   #don't forget about the corner case like when we come to the end of the char list 
                if(count == 1):
                    out_list.extend([prev])
                else:
                    out_list.extend([prev, *list(str(count))])
        #print(out_list)
        chars [:] = out_list[:] #As the problem expected the output list to be in place of the given chars list
        return ''.join(out_list)
if __name__ == "__main__":
    print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))