import collections
from typing import List


class Solution:
    """
    순환구조 여부를 파악하는 문제.
    dfs를 이용해서 순환구조를 판별한다.
        순환구조일 시 return False
    traced라는 set을 만들어서 탐색 중 traced에 현재 위치가 포함된다면 이미 방문한 것이므로 False를 return 한다.

    1. 일반 재귀
        일반적으로 재귀를 이용해 풀이했을 때 시간 초과가 발생했다.
        최적화를 위한 방안이 필요하다.
    2. 최적화
        visited라는 set을 두어 이미 방문한 곳이라면,
        순환구조 여부가 파악된 상태이기 떄문에 True를 return하는 가지치기를 이용해 최적화 하였다.
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        traced = set()
        visited = set()

        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(i):
            if i in traced:
                return False

            if i in visited:
                return True

            traced.add(i)

            for j in graph[i]:
                if not dfs(j):
                    return False

            traced.remove(i)
            visited.add(i)

            return True

        for i in list(graph):
            if not dfs(i):
                return False

        return True
