class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        global_max = float('-inf')

        for account in accounts:
            local_max = sum(account)
            global_max = max(global_max, local_max)
        
        return global_max
