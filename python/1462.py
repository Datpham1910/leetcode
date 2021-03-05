"""
1462. Course Schedule IV
Medium

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have direct prerequisites, for example, to take course 0 you have first to take course 1, which is expressed as a pair: [1,0]

Given the total number of courses n, a list of direct prerequisite pairs and a list of queries pairs.

You should answer for each queries[i] whether the course queries[i][0] is a prerequisite of the course queries[i][1] or not.

Return a list of boolean, the answers to the given queries.

Please note that if course a is a prerequisite of course b and course b is a prerequisite of course c, then, course a is a prerequisite of course c.

Example 1:

Input: n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: course 0 is not a prerequisite of course 1 but the opposite is true.
Example 2:

Input: n = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites and each course is independent.
Example 3:

Input: n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]
Example 4:

Input: n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
Output: [false,true]
Example 5:

Input: n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]
Output: [true,false,true,false]
 

Constraints:

2 <= n <= 100
0 <= prerequisite.length <= (n * (n - 1) / 2)
0 <= prerequisite[i][0], prerequisite[i][1] < n
prerequisite[i][0] != prerequisite[i][1]
The prerequisites graph has no cycles.
The prerequisites graph has no repeated edges.
1 <= queries.length <= 10^4
queries[i][0] != queries[i][1]
"""
from typing import List


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not prerequisites:
            return [False]*len(queries)
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, to_reach):
            if i == to_reach:
                return True
            if not graph[i]:
                return False
            return any(dfs(j, to_reach) for j in graph[i])

        return [dfs(i, j) for i, j in queries]

    def checkIfPrerequisite1(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res, map_ = [], {}
        graph = [[] for _ in range(n)]
        prev = [set() for _ in range(n)]
        degrees = [0] * n

        if not prerequisites:
            return [False] * n

        for p in prerequisites:
            graph[p[0]].append(p[1])
            degrees[p[1]] += 1
            prev[p[1]].add(p[0])

        queue = deque(list(filter(lambda i: degrees[i] == 0, range(n))))

        while queue:
            course = queue.popleft()
            for child in graph[course]:
                prev[child] |= prev[course]
                degrees[child] -= 1
                if not degrees[child]:
                    queue.append(child)

        for query in queries:
            res.append(query[0] in prev[query[1]])

        return res
