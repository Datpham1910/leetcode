"""
65. Valid Number
Hard

A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
At least one digit, followed by a dot '.'.
At least one digit, followed by a dot '.', followed by at least one digit.
A dot '.', followed by at least one digit.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
At least one digit.
For example, all the following are valid numbers:
["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], 
while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
Example 4:

Input: s = ".1"
Output: true
 

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        """
        "num" stands for numbers from 0 to 9.
        the double quotes, " ", stands for space

        S is start state
        P is pre-number, not yet a number
        D stands for decimal
        DN means decimal number
        N is number
        SC is scientific notation
        PS is pre-scientific notation number
        SN is scientific notation number
        NS is number w/ space
        """
        #construct DFA
        S = dict({"-":"P", "+":"P", "num":"N", " ":"S", ".":"D"})
        P = dict({"num":"N", ".":"D"})
        N = dict({"num":"N",".":"DN","e":"SC", " ":"NS"})
        D = dict({"num":"DN"})
        DN = dict({"e":"SC","num":"DN", " ":"NS"})
        SC = dict({"-":"PS", "+":"PS", "num":"SN"})
        PS = dict({"num":"SN"})
        SN = dict({"num":"SN", " ":"NS"})
        NS = dict({" ":"NS"})
        total_states = dict({"N":N, "DN":DN, "SN":SN, "S":S, "P":P, "D":D, "SC":SC, "PS":PS, "NS":NS})
        acc_states = set({"N", "DN", "SN", "NS"})
        
        #the starting state is S
        cur_state = "S"
        
        for indx in range(len(s)):
            input_type = s[indx]
            if s[indx] in '0123456789':
                input_type = "num"
            try:
                cur_state = total_states[cur_state][input_type]
            except: #if the transition is not defined, go to reject state
                return False
        
        if cur_state in acc_states:
            return True
        else:
            return False
