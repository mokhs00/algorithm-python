import collections
from typing import List


class Solution:
    """
    result.append()할 때 재귀 흐름을 이해하고 경로가 어떻게 쌓일지 예측하자.
    """

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        default_dict = collections.defaultdict(collections.deque)

        # place graph
        for a, b in sorted(tickets):
            default_dict[a].append(b)

        def dfs(current):
            while default_dict[current]:
                dfs(default_dict[current].popleft())
            result.append(current)

        dfs('JFK')

        return result[::-1]

    def findItinerary_use_stack(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(collections.deque)

        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].popleft())
            route.append(stack.pop())

        return route[::-1]
