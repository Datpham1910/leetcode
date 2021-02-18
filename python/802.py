'''
802. Find Eventual Safe States
Medium

We start at some node in a directed graph, and every turn, we walk along a directed edge of the graph. If we reach a terminal node (that is, it has no outgoing directed edges), we stop.

We define a starting node to be safe if we must eventually walk to a terminal node. More specifically, there is a natural number k, so that we must have stopped at a terminal node in less than k steps for any choice of where to walk.

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

The directed graph has n nodes with labels from 0 to n - 1, where n is the length of graph. The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph, going from node i to node j.

Example 1:

Illustration of graph
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
 

Constraints:

n == graph.length
1 <= n <= 104
0 <= graph[i].legnth <= n
graph[i] is sorted in a strictly increasing order.
The graph may contain self-loops.
The number of edges in the graph will be in the range [1, 4 * 104].
'''
from typing import List

from collections import defaultdict, compress
from typing import List


class Solution:
    WHITE, GRAY, BLACK = 0, 1, 2

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Find Eventual Safe States

        :param List[List[int]] G:
        :return List[int]:
        """

        N = len(graph)
        V = defaultdict(int)

        safe = [self.dfs(graph, V, u) for u in range(N)]
        return list(compress(range(N), safe))

    def dfs(self, graph, V, u) -> bool:
        """
        True    :   safe (i.e. non-cyclical)
        False   :   non-safe (i.e. cyclical)
        """
        V[u] = self.GRAY

        for nei in graph[u]:
            if V[nei] == self.WHITE and not self.dfs(graph, V, nei):
                # Cycle detected in descendant of `nei` - not safe!
                return False
            elif V[nei] == self.GRAY:
                # Cycle detected - not safe!
                return False

        V[u] = self.BLACK
        return True


    def eventualSafeNodes1(self, graph: List[List[int]]) -> List[int]:
        #safe = [None for i in range(len(graph))]
        def walk(i):
            if graph[i] == True:
                return True
            if graph[i] == False:
                return False
            
            if graph[i]==3:
                graph[i]=False
                return False
            
            if len(graph[i]) == 0:
                graph[i] = True
                return True
            
            edges = graph[i]
            graph[i]=3
            for j in edges:
                if not walk(j):
                    graph[i]=False
                    return False
            graph[i]=True
            return True
        for l in range(len(graph)):
            #print(safe)
            #print(notsafe)
            walk(l)
        return [i for i in range(len(graph)) if graph[i] ]
