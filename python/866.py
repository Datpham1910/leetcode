"""
866. Prime Palindrome
Medium

Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 

For example, 12321 is a palindrome.

Example 1:

Input: 6
Output: 7
Example 2:

Input: 8
Output: 11
Example 3:

Input: 13
Output: 101
 

Note:

1 <= N <= 10^8
The answer is guaranteed to exist and be less than 2 * 10^8.
"""
class Solution:
    def primePalindrome(self, k: int) -> int:
        if k < 12:
            for i in range(k, 12):
                if self.is_prime(i):
                    return i
        string_k = str(k)
        string_length = len(string_k)
        if string_length % 2 == 0:
            starting_root = 10**(string_length-string_length // 2)
        else:
            starting_root = int(string_k[:string_length-string_length // 2])
        for root in range(starting_root, 10**6):
            str_root = str(root)
            palindrome_gen = int(str_root + str_root[-2::-1])
            if palindrome_gen >= k and self.is_prime(palindrome_gen):
                return palindrome_gen

    def is_prime(self, n):
        return n > 1 and all(n % d for d in range(2, int(n**.5) + 1))