from typing import List

'''
1. dict(value:index) 형으로 데이터를 변경하고
2. nums를 탐색하면서 dict의 key와 일치하는 target - list[i]를 찾는다.
3. 그리고 그 값의 index를 return한다.
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            map[num] = i

        for i, num in enumerate(nums):
            index = target - num
            if index in map and i != map[index]:
                return [i, map[index]]
