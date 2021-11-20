from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        def dfs(current_sum, index, path):

            if current_sum > target:
                return
            if current_sum == target:
                result.append(path)

            for i in range(index, len(candidates)):
                dfs(current_sum + candidates[i], i, path + [candidates[i]])

        dfs(0, 0, [])

        return result
