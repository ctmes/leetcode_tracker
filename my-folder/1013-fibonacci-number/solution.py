class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        p, c = 0, 1

        for _ in range(2, n+1):
            p, c = c, p + c

        return c
        


        
