"""
1129. Shortest Path with Alternating Colors
Medium

Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]
Example 3:

Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]
Example 4:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]
Example 5:

Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]
 

Constraints:

1 <= n <= 100
red_edges.length <= 400
blue_edges.length <= 400
red_edges[i].length == blue_edges[i].length == 2
0 <= red_edges[i][j], blue_edges[i][j] < n
"""

from typing import List
from queue import Deque


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        dist = [float('inf')] * n
        dist[0] = 0
        re = {i: [] for i in range(n)}
        be = {i: [] for i in range(n)}

        for u, v in red_edges:
            re[u].append(v)

        for u, v in blue_edges:
            be[u].append(v)

        queue = Deque([(0, 0, 'b'), (0, 0, 'r')])
        vis = {(0, 'b'): True, (0, 'r'): True}

        while queue:
            node, level, color = queue.popleft()

            if color == 'b' or color == None:
                for neig in re[node]:
                    if (neig, "r") not in vis:
                        dist[neig] = min(dist[neig], level+1)
                        queue.append((neig, level+1, 'r'))
                        vis[(neig, 'r')] = True

            if color == 'r' or color == None:
                for neig in be[node]:
                    if (neig, "b") not in vis:
                        dist[neig] = min(dist[neig], level+1)
                        queue.append((neig, level+1, 'b'))
                        vis[(neig, 'b')] = True

        return [-1 if val == float('inf') else val for val in dist]
