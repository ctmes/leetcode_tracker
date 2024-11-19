class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        for j in jewels:
            total += stones.count(j)
        return total
