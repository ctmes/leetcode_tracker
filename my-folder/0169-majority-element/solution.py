class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        S = {}
        L = len(nums) // 2
        
        for num in nums:
            if num in S:
                if S[num] <= L:
                    S[num] += 1
            else:
                S[num] = 1
        
        return max(S, key=S.get)
        
