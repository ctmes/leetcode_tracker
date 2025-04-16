class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq = [0] * 60
        ans = 0
        
        # Count frequencies of remainders
        for t in time:
            freq[t % 60] += 1
        
        # Handle remainder 0 (pairs with themselves)
        ans += freq[0] * (freq[0] - 1) // 2
        
        # Handle remainder 30 (pairs with themselves)
        ans += freq[30] * (freq[30] - 1) // 2
        
        # Handle pairs of remainders r and 60-r
        for r in range(1, 30):
            ans += freq[r] * freq[60 - r]
        
        return ans
