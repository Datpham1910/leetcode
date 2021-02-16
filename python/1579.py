'''
1579. Remove Max Number of Edges to Keep Graph Fully Traversable
Hard

288

3

Add to List

Share
Alice and Bob have an undirected graph of n nodes and 3 types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can by traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if it's impossible for the graph to be fully traversed by Alice and Bob.

 

Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.

Constraints:

1 <= n <= 10^5
1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
edges[i].length == 3
1 <= edges[i][0] <= 3
1 <= edges[i][1] < edges[i][2] <= n
All tuples (typei, ui, vi) are distinct.
'''
from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(a):
            if f[a] != a:
                f[a] = find(f[a])
            return f[a]

        def union(a, b):
            fa = find(a)
            fb = find(b)

            if fa != fb:
                if d[fa] < d[fb]:
                    f[fb] = fa
                elif d[fa] > d[fb]:
                    f[fa] = fb
                else:
                    f[fb] = fa
                    d[fa] += 1
                return True
            else:
                return False

        d = list(range(n + 1))
        f = list(range(n + 1))
        ret = 0
        c1, c2 = 0, 0

        for t, u, v in edges:
            if t == 3:
                if union(u, v):
                    c1 += 1
                    c2 += 1
                else:
                    ret += 1

        f2 = f[:]
        d2 = d[:]

        for t, u, v in edges:
            if t == 1:
                if union(u, v):
                    c1 += 1
                else:
                    ret += 1

        f = f2
        d = d2
        for t, u, v in edges:
            if t == 2:
                if union(u, v):
                    c2 += 1
                else:
                    ret += 1

        #print(father, father2, c1, c2)
        return ret if c1 == c2 == n - 1 else -1

    def maxNumEdgesToRemove(self, n: int, e: List[List[int]]) -> int:
        def union(UF, u, v):
            UF[find(UF, v)] = find(UF, u)

        def find(UF, u):
            if UF[u] != u:
                UF[u] = find(UF, UF[u])
            return UF[u]

        def check(UF, t):
            UF = UF.copy()
            for tp, u, v in e:
                if tp == t:
                    if find(UF, u) == find(UF, v):
                        self.ans += 1
                    else:
                        union(UF, u, v)
            return len(set(find(UF, u) for u in UF)) == 1, UF

        ans, UF = 0, {u: u for u in range(1, n+1)}
        UF = check(UF, 3)[1]
        if not check(UF, 1)[0] or not check(UF, 2)[0]:
            return -1
        return ans

class UnionFindSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n
        self.size = 1
        
    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        elif self.ranks[pv] > self.ranks[pu]:
            self.parents[pu] = pv
        else:
            self.parents[pu] = pv
            self.ranks[pv] += 1
        self.size += 1
        return True
    
    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1, uf2, ans = UnionFindSet(n), UnionFindSet(n), 0
		
        for t, u, v in edges:
            if t != 3:
                continue
            if not uf1.union(u - 1, v - 1) or not uf2.union(u - 1, v - 1):
                ans += 1
        
        for t, u, v in edges:
            if t == 1 and not uf1.union(u - 1, v - 1):
                ans += 1
            elif t == 2 and not uf2.union(u - 1, v - 1):
                ans += 1
   
        return ans if uf1.size == n and uf2.size == n else -1s