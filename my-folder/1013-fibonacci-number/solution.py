class Solution:
    def fib(self, n: int) -> int:
        # memo = {0:0, 1:1}

        # def f(x):
        #     if x in memo:
        #         return memo[x]

        #     else:
        #         memo[x] =  f(x-1) + f(x-2)
        #         return memo[x]

        # return f(n)

        if n == 0:
            return 0

        if n == 1:
            return 1

        prev = 0
        cur = 1

        for i in range(2, n+1):
            prev, cur = cur, prev+cur

        return cur
