"""
218. The Skyline Problem
Hard

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

 

Example 1:


Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
 

Constraints:

1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings is sorted by lefti in non-decreasing order.
"""

from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        For me it was quite painful problem. I realized quite fast the main idea how you can solve it, but I spend like 2 hours to handling with all corner cases you can have here. So, the idea is the following: let us traverse our buildings from left to right and at each moment of time we decide what is height of current point. Howe we can do it? We need to keep two pieces of information:

        So-called active set: what buildings we currently have in given point.
        Also, we need to quickly determine the highest building in given point. We will use heap for this purpuse, and if we need to add new building to heap, it is not a problem, it can be done in O(log n). However, we can not easlily delete element from heap (in python you can do it with SortedList, quite powerful data structure), so we perform so-called lazy deletions from heap: it this way our heap can have buildings which already ended, but it does not matter.
        Now, let us go the the main algorithm:

        For each building, put two tuples of information to points: for left upper corner, we put x, y and also -1, meaning it is starting point and i: index of our building. For right upper corner we put exactly the same, but 1 instead of -1.
        Next, we sort our point by x coordinate. If it is equal, we sort them by height multiplied by -1 for left point and by 1 for right point. Why so strange: the reason, that we first want to process starts, from bigger to smaller, and then ends from smaller to bigger.
        Also, we put dummy element in our heap and set.
        Now, let us iterate through our points and: if we meet beginning of some building, we add it to active set, if we meet end, we remove it from active set
        If we meet left corner of building and also it is higher than we alredy met so far, that is h > -heap[0][0], then we add this element to ans. Also we add (-h, ind) to our heap (in python heaps are minimum heaps, so we need to keep negative heigth).
        If we meet right corner of building and it is less than highest current building, we do nothing with our heap: (actually, what we need to do is to say, that current building is not active any more and we already did this). Corner of building can not be more than than current highest building, because it is ending point. Finally, if h == -heap[0][0], it means, that we need to pop some element from our heap. How many? Here we have our lazy updates: we look if building is active or not and if it is not, we remove and continue, until we have highest building which is active. Finally, if new point we want to add has different height from what we have as the last element of our ans, we add new point to ans: [x, -heap[0][0]]: note, that we add point with height after we removed all inactive elements from heap.
        Just return our ans.
        Complexity: it is O(n log n), because for every corner we put and remove it from our heap only once, with time O(log n). Space complexity is potentially O(n).

        """
        points  = [(l,h,-1,i) for i, (l,r,h) in enumerate(buildings)]
        points += [(r,h,1,i) for i, (l,r,h) in enumerate(buildings)]
        points.sort(key = lambda x: (x[0], x[1]*x[2]))
        heap, active, ans = [(0,-1)], set([-1]), []
        
        for x, h, lr, ind in points:
            if lr == -1: active.add(ind)
            else: active.remove(ind)
           
            if lr == -1:
                if h > -heap[0][0]: 
                    ans.append([x, h])
                heappush(heap, (-h, ind))
            else:
                if h == -heap[0][0]:   
                    while heap and heap[0][1] not in active: heappop(heap)
                if -heap[0][0] != ans[-1][1]: 
                    ans.append([x, -heap[0][0]])
                
        return ans

    def getSkyline1(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(L, -H, R) for L, R, H in buildings]
        events += [(R, 0, 0) for _, R, _ in buildings]
        events.sort()
        
        res = [[0, 0]] # result, [x, height]
        live = [(0, float("inf"))] # heap, (-height, ending position)
        
        for pos, negH, R in events:
            while live[0][1] <= pos:
                heappop(live)
            if negH:
                heappush(live, (negH, R))
                
            if res[-1][1] != -live[0][0]:
                res.append([pos, -live[0][0]])
        
        return res[1:]