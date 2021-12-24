from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(arr, index, sum):

            if sum > target:
                return
            if sum == target:
                result.append(arr)
                return

            for i in range(index, len(candidates)):
                dfs(arr + [candidates[i]], i, sum + candidates[i])

        dfs([], 0, 0)

        return result
