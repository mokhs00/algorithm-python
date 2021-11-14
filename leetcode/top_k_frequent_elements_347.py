import collections
import heapq
from typing import List


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = collections.Counter(nums)
        answer_heap: heapq = []

        for f in frequency:
            heapq.heappush(answer_heap, (-frequency[f], f))

        answer: list = list()

        for _ in range(k):
            answer.append(heapq.heappop(answer_heap)[1])
        return answer

    # pythonic way
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     frequency = collections.Counter(nums)
    #     answer = list(zip(*frequency.most_common(k)))[0]
    #
    #     return answer
