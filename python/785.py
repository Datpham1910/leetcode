'''
785. Is Graph Bipartite?
Medium

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Example 1:

Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

Constraints:

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
'''
from typing import List
from collections import defaultdict, deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        This problem is very similar to problem 886. Possible Bipartition and it happens that I already solved this problem previously, you can see my solution here: https://leetcode.com/problems/possible-bipartition/discuss/654840/Python-Simple-dfs-traversal-O(E%2BV)-detailed-explanations

        Here I do absolutely the same idea, but with a bit more clear coding style and also we do not need to create adjacency list here, it is already given in this way. The idea is the following: we traverse our graph and color our nodes int two colors 0 and 1: first one for nodes which can be reached with even number of steps and 1 for odd number of steps. Also we keep self.loop flag, which is true if we found odd loop, that is our graph is not bipartite.

        We define dist array with -1 inside and then we start dfs from every node, and color our graph (note, that graph can have several connected components, so we need to start dfs from all nodes).

        Complexity: time complexity is O(E+V), because it is complexity of classical dfs we are using. Space complexity is O(V) to keep dist array. Here E is number of edges and V is number of vertices.

        '''

        def dfs(start):
            if self.loop:
                return  # early stop if we found odd cycle

            for neib in graph[start]:
                if dist[neib] >= 0 and dist[neib] == dist[start]:
                    self.loop = True
                elif dist[neib] < 0:
                    dist[neib] = dist[start] ^ 1
                    dfs(neib)

        n = len(graph)
        self.loop, dist = False, [-1] * (n)

        for i in range(n):
            if self.loop:
                return False  # early stop if we found odd cycle
            if dist[i] == -1:
                dist[i] = 0
                dfs(i)

        return True

    def isBipartite1(self, graph: List[List[int]]) -> bool:
        tags = defaultdict(int)
        for i in range(len(graph)):
            if i not in tags:
                queue = deque([i])
                tags[i] = 1
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor in tags:
                            if tags[neighbor] == tags[node]:
                                return False
                        else:
                            tags[neighbor] = (tags[node] * (-1))
                            queue.append(neighbor)
