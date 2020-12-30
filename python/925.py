"""
925. Long Pressed Name
Easy

Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
 

Constraints:

1 <= name.length <= 1000
1 <= typed.length <= 1000
name and typed contain only lowercase English letters.
"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        # two pointers to the "name" and "typed" string respectively
        np, tp = 0, 0

        # advance two pointers, until we exhaust one of the strings
        while np < len(name) and tp < len(typed):
            if name[np] == typed[tp]:
                np += 1
                tp += 1
            elif tp >= 1 and typed[tp] == typed[tp-1]:
                tp += 1
            else:
                return False

        # if there is still some characters left *unmatched* in the origin string,
        #   then we don't have a match.
        # e.g.  name = "abc"  typed = "aabb"
        if np != len(name):
            return False
        else:
            # In the case that there are some redundant characters left in typed
            # we could still have a match.
            # e.g.  name = "abc"  typed = "abccccc"
            while tp < len(typed):
                if typed[tp] != typed[tp-1]:
                    return False
                tp += 1

        # both strings have been consumed
        # Time complexity: O(n)
        # Extra space complexity: O(1)
        return True

    def isLongPressedName1(self, name: str, typed: str) -> bool:
        name=list(name)
        typed= list(typed)
        
        while name:
            i, j=0,0
            n=name[0]
            while name and name[0]==n:
                i+=1
                name.pop(0)
            while typed and typed[0]==n:
                j+=1
                typed.pop(0)
                
            if j<i:
                return False 
        if typed:
            return False
    
        return True
if __name__ == "__main__":
    print(Solution().isLongPressedName(name = "leelee", typed = "lleeelee"))