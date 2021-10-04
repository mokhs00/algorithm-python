from typing import List

'''
% 주의 : 나눗셈 연산을 하지 않고 O(n)에 풀어야 함
왼쪽값을 계산해서 차곡차곡 쌓아두고
오른족값을 계산
이렇게하면 index i를 제외하고 모든 값이 곱해짐
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        temp = 1
        for i in range(len(nums)):
            result.append(temp)
            temp *= nums[i]

        temp = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            result[i] *= temp
            temp *= nums[i]
        return result
