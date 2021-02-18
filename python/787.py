"""
787. Cheapest Flights Within K Stops
Medium

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""
from typing import List
import collections
import heapq


class Solution(object):
	def findCheapestPrice(self, n, flights, src, dst, K):
		graph = collections.defaultdict(list)
		pq = []
		for u, v, w in flights:
			graph[u].append((w, v))
			heapq.heappush(pq, (0, K+1, src))

			while pq:
				price, stops, city = heapq.heappop(pq)

				if city is dst:
					return price
				if stops > 0:
					for price_to_nei, nei in graph[city]:
						heapq.heappush(pq, (price+price_to_nei, stops-1, nei))
		return -1

	def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
		# Use Dijstra's algorithm. The only difference is that, we need to reconsider a node if we need to re-consider it the number of stops is less than before.

		# Build the adjacency matrix
		adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
		for s, d, w in flights:
			adj_matrix[s][d] = w

		# Shortest distances array
		distances = [float("inf") for _ in range(n)]
		current_stops = [float("inf") for _ in range(n)]
		distances[src], current_stops[src] = 0, 0

		# Data is (cost, stops, node)
		minHeap = [(0, 0, src)]

		while minHeap:

			cost, stops, node = heapq.heappop(minHeap)  # we process the node with minimum cost first

			# If destination is reached, return the cost to get here
			if node == dst:
				return cost

			# If there are no more steps left, continue
			if stops == K + 1:
				continue

			# Examine and relax all neighboring edges if possible
			for nei in range(n):
				if adj_matrix[node][nei] > 0:  # node->nei exists
					dU, dV, wUV = cost, distances[nei], adj_matrix[node][nei]

					# Better cost?
					if dU + wUV < dV:
						distances[nei] = dU + wUV  # update the cost
						current_stops[nei] = stops + 1
						heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
					elif stops < current_stops[nei]:
						# If it is not a better cost, but better stops?
						current_stops[nei] = stops + 1
						heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))

		return -1 if distances[dst] == float("inf") else distances[dst]

	def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
		# Gợi ý: Thay đổi hàm Dijkstra.
		# Thay vì sử dụng điều kiện là giá rẻ nhất để cập nhật thì
		# sử dụng điều kiện là số stops hiện tại nhỏ hơn k.
		graph = [[] for _ in range(n)]
		for flight in flights:
			u, v, w = flight
			graph[u].append((v, w))
		inf = float('inf')
		dist = [inf for _ in range(n)]

		def dijkstra(src):
			minHeap = []
			dist[src] = 0
			heapq.heappush(minHeap, (0, src, 0))
			while minHeap:
				u = heapq.heappop(minHeap)
				uWeight, uID, uCnt = u
				if uID == dst:
					return uWeight
				for v in graph[uID]:
					vID, vWeight = v
					if uCnt <= K:
						dist[vID] = uWeight + vWeight
						heapq.heappush(minHeap, (uWeight + vWeight, vID, uCnt + 1))
			return -1
		return dijkstra(src)
