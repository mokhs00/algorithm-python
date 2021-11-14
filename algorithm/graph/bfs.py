from collections import deque
from typing import Deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def iterative_bfs(start_v):
    discovered = [start_v]
    queue: Deque = deque()
    queue.appendleft(start_v)

    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.appendleft(w)

    return discovered

# print(iterative_bfs(1))
