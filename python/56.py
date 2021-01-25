"""
56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        # Time complexity : O(n\log{}n)O(nlogn)
        # Other than the sort invocation, we do a simple linear scan of the list, so the runtime is dominated by the O(n\log{}n)O(nlogn) complexity of sorting.
        # Space complexity : O(\log N)O(logN) (or O(n)O(n))
        return merged

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: [x[0], x[1]])
        print(intervals)
        stack = [intervals[0]]
        for idx in range(1, len(intervals)):
            if intervals[idx][0] <= stack[-1][1]:
                if intervals[idx][1] > stack[-1][1]:
                    item = stack.pop()
                    stack.append([item[0], intervals[idx][1]])
            else:
                stack.append(intervals[idx])
        return stack


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
