from typing import List

'''
- 투 포인터를 이용한다. 왼쪽과 오른쪽에서 각각 출발해 서로 만날때까지 중앙으로 이동한다.
- 핵심은 가장 바깥쪽의 가장 높은 막대의 높이이다. 결국 물이 차는 양은 이 막대들이 결정한다.
1. left, right를 선언하고 left < right 일 때까지(만나기 전까지) 다음 연산을 반복한다.
  - left_max <= right_max 라면, left 에서 한 칸씩 이동하고, 
    (left_max - height[left])를 result 에 추가한다.  
  - 반대 경우에는 right 를 기준으로 위 연산을 수행한다.
  - 참고로 둘이 같은 경우는 어느쪽이 이동해도 상관없기에 left에서 수행하기로 한다.
2. 1번 연산이 종료되면, result를 반환한다. 
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        result = 0
        left, right = 0, len(height) - 1

        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            if left_max <= right_max:
                result += left_max - height[left]
                left += 1
            else:
                result += right_max - height[right]
                right -= 1

        return result
