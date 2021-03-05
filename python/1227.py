"""
1227. Airplane Seat Assignment Probability
Medium

n passengers board an airplane with exactly n seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of passengers will:

Take their own seat if it is still available, 
Pick other seats randomly when they find their seat occupied 
What is the probability that the n-th person can get his own seat?

 

Example 1:

Input: n = 1
Output: 1.00000
Explanation: The first person can only get the first seat.
Example 2:

Input: n = 2
Output: 0.50000
Explanation: The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).
 

Constraints:

1 <= n <= 10^5
"""

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        """
        Let us suppose n>1
        Now let us suppose first person goes and sits on k position. 
        Now we surely know that person(2 to k-1) will sit on their correct position
        (Because when person 2 to k-1 comes then they will find their place empty and will sit on their respective seats). Now k'th person has 3 choices

        Sit on seat 1 in which case last person will surely sit on his seat.
        Sit on last seat in which case last person will surely not sit on his seat.
        Sit on some seat from k+1 to n-1.
        Now if he takes option 3 then he will sit on some seat say "j". Now j will again have three options to sit.
        This cycle will continue and every person can sit on first and last seat will equal probability. Hence the probability will be 0.5
        """
        if(n==1):
            return(1.0)
        else:
            return(0.5)