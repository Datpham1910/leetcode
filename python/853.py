"""
853. Car Fleet
Medium

N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

How many car fleets will arrive at the destination?

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Note:

0 <= N <= 10 ^ 4
0 < target <= 10 ^ 6
0 < speed[i] <= 10 ^ 6
0 <= position[i] < target
All initial positions are different.
"""
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        ans = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]: ans += 1  # if lead arrives sooner, it can't be caught
            else: times[-1] = lead # else, fleet arrives at later time 'lead'

        return ans + bool(times) # remaining car is fleet (if it exists)

    
    def carFleet1(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_speed = [(position[i], speed[i]) for i in range(len(position))]
        pos_and_speed.sort(key=lambda x: x[0])
        etas = [(target - pos) / sp for pos, sp in pos_and_speed]
        result = 0
        current_eta = 0
        for eta in etas[::-1]:
            if eta > current_eta:
                result += 1
                current_eta = eta
        return result

    def carFleet2(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_indices = sorted(range(len(position)), key=lambda x: position[x], reverse=True)
        last = -1
        fleets = 0
        for i in sorted_indices:
            time_to_target = (target-position[i])/float(speed[i])
            if time_to_target > last:
                last = time_to_target
                fleets += 1
        return fleets

if __name__ == "__main__":
    print(Solution().carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
