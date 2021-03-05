"""
640. Solve the Equation
Medium

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
"""

class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str

        The idea is to reduce the equation to the list of individual terms ax + bx + cx .. + aa + bb + cc = 0
        We can represent the equation above in the form of a list of tuples of (term, sign) .. We first eliminate = , 
        then +'es and then finally all the -'es to end up with the list like above.

        Finally we reduce the list to the form of ax + b = 0

        Based on rules of linear equations, if a != 0, there exists a unique solution. If a = 0, 
        then there are infinite solutions if b = 0 also. If b != 0, then there are no solutions.

        IMO, this solution is acceptable in an interview, wheras using regex and eval might not be feasible.
        """
        # Equation is represented by list of tuples;
        # Each element in the list is (expression, sign) ;; sign is True for positive, False for negative
        
        # Eliminate '=' first to separate right hand side and left hand side
        [left, right] = equation.split('=')
        
        # Eliminate '+' next; carry over sign
        eq, next_eq = [(left, True), (right, False)], []
        for (term , sign) in eq:
            splits = term.split('+')
            for split in splits:
                next_eq.append((split, sign))
                
        # Eliminate '-' next; carry over sign ; Pay special attention to negative numbers
        eq, next_eq = next_eq, []
        for (term , sign) in eq:
            splits = term.split('-')
            if term[0] != '-':
                next_eq.append((splits[0], sign))
            for split in splits[1:]:
                next_eq.append((split, not sign))
        
        # Get the equation in the form of ax + b = 0; i.e compute a and b
        # note that 'x' = 1x 
        eq = next_eq
        a = b = 0
        for (term,sign) in eq:
            if term[-1] == 'x':
                num_term = term[:-1]
                num = int(num_term) if num_term != '' else 1
                a += num if sign else (-num)
            else:
                num = int(term)
                b += num if sign else (-num)
        
        if a == 0:
            return "Infinite solutions" if b == 0 else "No solution"
        else:
            return "x="+str(-b//a)