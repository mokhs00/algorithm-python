import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        size = len(nums)

        result = []

        def dfs(prev_list: List, num_list: List[int]):

            if len(prev_list) == size:
                result.append(prev_list)
                return

            for num in num_list:
                temp_list = num_list[:]
                temp_list.remove(num)
                dfs(prev_list + [num], temp_list)

        dfs([], nums)

        return result

    def permute_2(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []

        def dfs(num_list: List):
            if len(num_list) == 0:
                result.append(prev_elements[:])

            for num in num_list:
                next_list = num_list[:]
                next_list.remove(num)

                prev_elements.append(num)
                dfs(next_list)
                prev_elements.pop()

        dfs(nums)

        return result

    def permute_3(self, nums: List[int]) -> List[List[int]]:
        '''
        구현의 효율성, 성능을 위한 itertools 사용.
        효율적으로 설계된 C 라이브러리이므로 속도에 이점이 있음.
        + 직접 구현하는 것보다 버그 발생 가능성 낮음

        => 실무에서는 사용하지 않을 이유가 없다.
        '''
        return list(itertools.permutations(nums))