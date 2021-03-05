"""
1042. Flower Planting With No Adjacent
Medium

You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. In each garden, you want to plant one of 4 types of flowers.

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

Example 1:

Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Explanation:
Gardens 1 and 2 have different types.
Gardens 2 and 3 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].
Example 2:

Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 

Constraints:

1 <= n <= 104
0 <= paths.length <= 2 * 104
paths[i].length == 2
1 <= xi, yi <= n
xi != yi
Every garden has at most 3 paths coming into or leaving it.
"""
from typing import List
import defaultdict


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        for path in paths:
            G[path[0]].append(path[1])
            G[path[1]].append((path[0]))
        colored = defaultdict()

        def dfs(G, V, colored):
            colors = [1, 2, 3, 4]
            for neighbour in G[V]:
                if neighbour in colored:
                    if colored[neighbour] in colors:
                        colors.remove(colored[neighbour])
            colored[V] = colors[0]

        for V in range(1, N + 1):
            dfs(G, V, colored)

        ans = []
        for V in range(len(colored)):
            ans.append(colored[V + 1])

        return ans

    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(N+1)]
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        result = []
        for i in range(1, N+1):
            flowers = set(range(1, 5))
            for otherGarden in graph[i]:
                if otherGarden < i:
                    flowers.discard(result[otherGarden-1])
            result.append(flowers.pop())
        return result
