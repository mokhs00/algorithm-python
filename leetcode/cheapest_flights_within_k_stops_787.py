import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append([v, w])

        visit = {}
        Q = [(0, src, 0)]
        while Q:
            price, node, k_ = heapq.heappop(Q)
            if node == dst:
                return price
            if node not in visit or visit[node] > k_:
                visit[node] = k_
                for v, w in graph[node]:
                    if k_ <= k:
                        alt = price + w
                        heapq.heappush(Q, (alt, v, k_ + 1))
        return -1
