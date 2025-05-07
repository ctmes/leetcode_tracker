class Solution:
    def numberOfSteps(self, num: int) -> int:
        def helper(i, steps):
            if i == 0:
                return steps

            if i % 2 == 0:
                return helper(i/2, steps+1)
            else:
                return helper(i-1, steps+1)

        return helper(num, 0)
