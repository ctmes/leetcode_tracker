class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev, cur = 0,0

        for i in range(2, n+1):
            # dp[i] = min((dp[i-2] + cost[i-2]), (dp[i-1] + cost[i-1]))
            prev, cur = cur, min(cost[i-2] + prev, cost[i-1] + cur) # prev = i-2, cur = i-1

        return cur
