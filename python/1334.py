"""
1344. Angle Between Hands of a Clock
Medium 

Example 1:



Input: hour = 12, minutes = 30
Output: 165
Example 2:



Input: hour = 3, minutes = 30
Output: 75
Example 3:



Input: hour = 3, minutes = 15
Output: 7.5
Example 4:

Input: hour = 4, minutes = 50
Output: 155
Example 5:

Input: hour = 12, minutes = 0
Output: 0
 

Constraints:

1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.
"""

class Solution(object):
    def angleClock(self, hour, minutes):

        angle_min=minutes/5
        angle_hour=minutes/60+hour
        
        diff=abs(angle_min-angle_hour)*360/12
        
        return min(diff,360-diff)