'''
399. Evaluate Division
Medium

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
'''

from typing import List, Tuple
import collections


class Solution:
    '''    
    We can treat each equation as an edge, variables as nodes and value as weight, and build a weighted graph. Then for each queries (x, y), we try to find a path from x to y. The answer is the product of all edges' weights. If either x or y is not in graph or x and y are not connected in graph, the answer doesn't exist.
    We can use a defaultdict(dict) G to build a weighted graph and G[x][y] will be the weight of edge x->y which is the value of x / y

    So one solution is BFS (or DFS) for each query.
    '''

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        G = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            G[x][y] = v
            G[y][x] = 1/v

        def bfs(src, dst):
            if not (src in G and dst in G):
                return -1.0
            q, seen = [(src, 1.0)], set()
            for x, v in q:
                if x == dst:
                    return v
                seen.add(x)
                for y in G[x]:
                    if y not in seen:
                        q.append((y, v*G[x][y]))
            return -1.0
        return [bfs(s, d) for s, d in queries]

    def calcEquation1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        Another solution is Union Find.
        Our root map is root and each root[x] is in form of (root(x), ratio) where ratio = x/root(x). If x == root(x), then ratio = 1.0. So just consider root as a denominator here. Then, we process the equations. For each x/y = v, we union x to y or set root(root(x)) = root(y) as y is the denominator. After union all x, y in the equations, for each a, b in the queries, if a and b are not in the same union set, then a and b are not transmissable to each other so a/b should return -1.0.

        Now that we have a ratio element in each root[x], we need to update it in find() and union() as well.
        In find(x), we have root[x] = (p, x/p) where p is the parent node of x and not neccessarily the root node. But we will do path compression and recursively update all the parent nodes in the path to root. And ratio should be updated as well. Eventually find(p) returns updated root[p] = (root(p), p/root(p)).
        So root[x] should be updated to (root(x), x/root(x)) = (root(p), x/p * p/root(p))) = (root[p][0], root[x][1] * root[p][1])

        For union(x, y) in equations processing, we make root(root(x)) = root(y) as mentiond previously. And for root[root(x)]'s ratio, as root(y) is root(x)'s new root, we update it to root(x)/root(y) = (x/y) * (y/root(y)) / (x/root(x)) = x/y * root[y][1] / root[x][1]. x/y is the provided equation outcome value.

        For union(x, y) in queries, we can just simply return x/y = (x/root(x)) / (y/root(y)) = root[x][1]/root[y][1].
        '''
        root = {}

        # xr = x/parent(x), pr = parent(x)/root(x), update xr to xr*pr = x/root(x)
        def find(x):
            p, xr = root.setdefault(x, (x, 1.0))
            if x != p:
                r, pr = find(p)
                root[x] = (r, xr*pr)
            return root[x]

        # if root(x) = root(y), equations "x / y" doable as (x/root(x)) / (y/root(y)) = xr / yr
        def union(x, y, ratio):
            px, xr, py, yr = *find(x), *find(y)
            if not ratio:
                return xr / yr if px == py else -1.0
            if px != py:
                root[px] = (py, yr/xr*ratio)

        for (x, y), v in zip(equations, values):
            union(x, y, v)
        return [union(x, y, 0) if x in root and y in root else -1.0 for x, y in queries]


# # Time complexity - O(MN) for M queries
# # Space complexity - O(2N) for outgoing + O(M*N) visited + O(N) queue
# from collections import deque
# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
#         def def_graph(): # O(N)
#             for i, equation in enumerate(equations):
#                 if equation[0] not in outgoing:
#                     outgoing[equation[0]] = dict()
#                 if equation[1] not in outgoing:
#                     outgoing[equation[1]] = dict()
#                 outgoing[equation[0]][equation[1]] = values[i]
#                 outgoing[equation[1]][equation[0]] = 1/values[i]
        
        
#         def bfs(query): # O(N)
#             visited = {node: False for node in outgoing}
#             src, dest = query
            
#             # edge case
#             if src not in outgoing: 
#                 return -1
            
#             q = deque([(src, 1)])
#             visited[src] = True
            
#             while q:
#                 node, mul_ = q.popleft()
#                 if node==dest:   # if you have reached the dest, return 
#                     return mul_
                
#                 if node not in outgoing:
#                     continue
                
#                 for edge in outgoing[node]:
#                     if not visited[edge]:
#                         q.append((edge, mul_ * outgoing[node][edge]))
#                         visited[edge] = True
                
#             return -1
        
#         # edge case
#         if not queries:
#             return 
        
#         # logic 
#         #1. create graph containing  outgoing edges
#         outgoing = dict()
#         def_graph()
        
#         #2. Perform BFS traversal
#         res = []
#         for query in queries:
#             res.append(bfs(query))
        
#         return res
            
    
                
# Time complexity - O(MN) for M queries
# Space complexity - O(2N) for outgoing + O(M*N) visited + O(N) queue
from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def def_graph(): # O(N)
            for i, equation in enumerate(equations):
                if equation[0] not in outgoing:
                    outgoing[equation[0]] = dict()
                if equation[1] not in outgoing:
                    outgoing[equation[1]] = dict()
                outgoing[equation[0]][equation[1]] = values[i]
                outgoing[equation[1]][equation[0]] = 1/values[i]
        
        
        def dfs(curr, dest, mul_): # O(N)
            if curr==dest:   # if you have reached the dest, return 
                return mul_
               
            ret = -1
            for nei in outgoing[curr]:
                if not visited[nei]:
                    visited[nei] = True
                    ret = dfs(nei, dest, mul_*outgoing[curr][nei])
                    visited[nei] = False
                    if ret!=-1:
                        break
                
            return ret
        
        
        # edge case
        if not queries:
            return 
        
        # logic 
        #1. create graph containing  outgoing edges
        outgoing = dict()
        def_graph()
        
        #2. Perform BFS traversal
        res = []
        visited = {node: False for node in outgoing}
        for query in queries:
            src, dest = query
            # edge case
            if src not in outgoing or dest not in outgoing: 
                res.append(-1)
                continue
            ret = dfs(src, dest, 1)
            res.append(ret)
        
        return res
            