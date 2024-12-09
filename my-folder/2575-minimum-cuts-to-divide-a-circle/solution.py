class Solution:
    def numberOfCuts(self, n: int) -> int:
        # n = 1
        if n == 1:
            return 0

        # n = 2
        if n == 2:
            return 1

        if n % 2 == 0:
            return int(n / 2)
        
        if n % 2 != 0:
            return n
