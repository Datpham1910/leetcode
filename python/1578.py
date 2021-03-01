"""
1578. Minimum Deletion Cost to Avoid Repeating Letters
Medium

Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

Example 1:

Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
Example 2:

Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.
Example 3:

Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").
 

Constraints:

s.length == cost.length
1 <= s.length, cost.length <= 10^5
1 <= cost[i] <= 10^4
s contains only lowercase English letters.
Accepted
"""


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        """
        Explanation
        The idea is to loop through each input character and whenever it is not equal to the one which is marked as active, the local costs are added to the output and the local maximum cost is subtracted from it since we do not need to delete all the encountered adjacent characters which are the same. The local costs and maximum cost are then set to the one which is required to remove the given character which is going to be marked as active. Every time the active character is encountered, its corresponding cost is added to the local costs and the local maximum cost is updated if the given cost is higher.

        Runtime Complexity
        O(n) since each input character is examined once.

        Space Complexity
        O(1)

        Python Implementation"""
        costs = cost[0]
        maximum_cost = cost[0]
        start_index = 0
        output = 0
        
        for i in range(1, len(s)):
            if s[i] != s[start_index]:
                output += costs - maximum_cost
                maximum_cost = 0
                costs = 0
                start_index = i
                
            maximum_cost = max(maximum_cost, cost[i])
            costs += cost[i]
            
        return output + costs - maximum_cost