from typing import List
'''
stack 에는 index 를 담고 -> index 로 temperaetures 에서 값을 조회하기 위함
answer[]에 기본 값으로 0을 채워둔다.
temperatures 를 탐색하며 stack[-1] 값과 비교하여 stack[-1]이 현재 temperature 보다 값이 크다면, 
기존에 stack 에 있던 값을 pop 하고 last라는 변수에 담아두고,
 (현재 temperature 의 index) - (stack[-1]) 값을 answer[last] 에 기록한다. 
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer
