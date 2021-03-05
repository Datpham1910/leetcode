"""
765. Couples Holding Hands
Hard

N couples sit in 2N seats arranged in a row and want to hold hands. 
We want to know the minimum number of swaps so that every couple is sitting side by side. 
A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, 
the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.
"""
from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        """
        Idea: First construct a dictionary mapping each person to the index at which he/she sits. Then we iterate over row and greedily construct the solution, i.e., for each i % 2 == 0, we swap row[i+1] with the correct person so that row[i+1] forms a couple with row[i]. The total number of such swaps is the minimum number of swaps to make the couples sit together.

        We illustrate the algorithm with an example:

        initialize: row = [0,2,4,6,7,1,3,5], dic = {0:0, 2:1, 4:2, 6:3, 7:4, 1:5, 3:6, 5:7}
        i = 0: row = [0,1,4,6,7,2,3,5], dic = {0:0, 1:1, 4:2, 6:3, 7:4, 2:5, 3:6, 5:7}
        i = 2: row = [0,1,4,5,7,2,3,6], dic = {0:0, 1:1, 4:2, 5:3, 7:4, 2:5, 3:6, 6:7}
        i = 4: row = [0,1,4,5,7,6,3,2], dic = {0:0, 1:1, 4:2, 5:3, 7:4, 6:5, 3:6, 2:7}
        i = 6: row = [0,1,4,5,7,6,3,2], dic = {0:0, 1:1, 4:2, 5:3, 7:4, 6:5, 3:6, 2:7}
        Time complexity: O(n), space complexity: O(n).

        """
        dic = {x:i for i,x in enumerate(row)}
        res = 0
        for i, n in enumerate(row):
            if i % 2 == 0:
                if n % 2 == 1:
                    if row[i+1] != n-1:
                        tmp = dic[n-1]
                        row[dic[n-1]], row[i+1] = row[i+1], row[dic[n-1]]
                        dic[row[i+1]] = i+1
                        dic[row[tmp]] = tmp
                        res += 1
                else:
                    if row[i+1] != n+1:
                        tmp = dic[n+1]
                        row[dic[n+1]], row[i+1] = row[i+1], row[dic[n+1]]
                        dic[row[i+1]] = i+1
                        dic[row[tmp]] = tmp
                        res += 1
        return res

    def minSwapsCouples1(self, row: List[int]) -> int:
        idx = [0 for _ in range(len(row))]
        
        for i in range(len(row)):
            idx[row[i]] = i
        
        cnt = 0
        for i in range(1, len(row), 2):
            partner = row[i]^1
            if row[i-1] != partner:
                p_idx = idx[partner]
                row[i-1], row[p_idx] = row[p_idx], row[i-1]
                idx[row[p_idx]] = p_idx
                cnt += 1
                
        return cnt