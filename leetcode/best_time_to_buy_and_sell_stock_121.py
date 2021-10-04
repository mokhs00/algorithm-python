import sys
from typing import List

'''
왼쪽에서부터 오른쪽으로 지나온 값들 중 가장 최소 값에서 현재 가격을 뺀 것을
max_profit 과 비교해서 max_profit 을 항상 갱신한다.
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
