from typing import List

'''
정렬해놓으면 항상 0 2 4 이렇게 짝수 번째 index 를 가진 값이 작은 값이 된다.
'''

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
