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
