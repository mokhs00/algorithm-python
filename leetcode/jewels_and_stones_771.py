import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0
        for char in jewels:
            count += freqs[char]

        return count

    # pythonic way
    # def numJewelsInStones(self, jewels: str, stones: str) -> int:
    #     return sum(s in jewels for s in stonesZ
