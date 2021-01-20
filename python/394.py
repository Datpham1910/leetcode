"""
394. Decode String
Medium

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""


class Solution:
    def decodeString(self, s: str) -> str:
        """
        The solution is a simple stack based one which evalutes the innermost brackets first. 
        You iterate through the string, and push everything to a stack until you've found a right bracket. 
        Once you've found a right bracket, you use that and pop from the stack to evaluate the innermost expression in the string. 
        For example, if you have 2[a3[b]], your stack would be [2, "[", "a", 3, "[", "b"] when it reaches the first right bracket. 
        Once it reaches the first right bracket, it attempts to evaluate everything in the innermost bracket by popping from the stack to form the entire string you need to multiply, and finding the number you need to multiply by. 
        After this, the stack will look like: [2, "[", "a", "bbb" ]. 
        The innermost expression of 3, "[", "b" was turned into bbb and put back into the stack. 
        At the next right bracket, we will similarily evaluate the innermost bracket , so that the stack turns into ["abbbabbb"]. 
        If there are multiple sets of enclosed brackets in the expression, our stack will end up with multiple strings in the end. Simply join them for the result.
        Args:
            s (str): [description]

        Returns:
            str: [description]
        """
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                current = ''
                while stack:
                    val = stack.pop()
                    if val == "[":
                        break
                    current = val + current
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*current)
            else:
                stack.append(s[i])
        return ''.join(stack)
