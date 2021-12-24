import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for i, j in sorted(tickets, reverse=True):
            graph[i].append(j)

        route = []

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            route.append(start)

        dfs('JFK')
        return route[::-1]