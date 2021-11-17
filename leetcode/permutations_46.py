from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        size = len(nums)

        result = []

        def dfs(prev_list: List, num_list: List[int]):

            if len(prev_list) == size or num_list is None:
                result.append(prev_list)
                return

            for num in num_list:
                temp_list = num_list[:]
                temp_list.remove(num)
                dfs(prev_list + [num], temp_list)

        dfs([], nums)

        return result
