from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def dfs(index, path):

            if len(digits) == len(path):
                answer.append(path)
                return

            for i in range(index, len(digits)):
                for letter in letters[digits[i]]:
                    dfs(i + 1, path + letter)

        letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        answer = []

        if not digits:
            return []

        dfs(0, "")

        return answer
