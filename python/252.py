from typing import List
class Solution:
    def can_attend_meeting(self, intervals: List[List[int]]) -> bool:
        if not intervals: return False
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
        # Time: NlogN
        # Extra Space: O(N)
if __name__ == "__main__":
    print(Solution().can_attend_meeting([[0,30],[5,10],[15,20]]))
    print(Solution().can_attend_meeting([[0, 5],[5,10],[15,20]]))
    print(Solution().can_attend_meeting([[7,10],[2,4]]))