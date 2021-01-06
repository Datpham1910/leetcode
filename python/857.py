"""
857. Minimum Cost to Hire K Workers
Hard

There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
 

Note:

1 <= K <= N <= 10000, where N = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000
Answers within 10^-5 of the correct answer will be considered correct.
"""
import heapq
from typing import List
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted((w/q, w, q) for w, q in zip(wage, quality))
        cost, team, sumq = float('inf'), [], 0
        for ratio, w, q in workers:
            heapq.heappush(team, -q)
            sumq += q
            if len(team) > K: sumq += heapq.heappop(team)
            if len(team) == K: cost = min(cost, sumq * ratio)   
        return cost

    def mincostToHireWorkers2(self, quality: List[int], wage: List[int], K: int) -> float:
        N = len(wage)
        cost_per_qulity = [float(wage[i])/quality[i] for i in range(N)]        
        workers = sorted(zip(quality, cost_per_qulity), key = lambda x: x[1])
        
        
        pq = [-q[0] for q in workers[:K]]
        heapq.heapify(pq)        
        qsum = -sum(pq)
        cost_min = workers[K-1][1] * qsum
        for i in range(K, N):
            if workers[i][0] < -pq[0]:
                qsum = qsum + workers[i][0] + pq[0]                
                cost_min = min(cost_min, qsum * workers[i][1])
                heapq.heapreplace(pq, -workers[i][0])                
        
        return cost_min

if __name__ == "__main__":
    print(Solution().mincostToHireWorkers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3))