class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        MIN = float('inf')
        l = 0
        summ = 0

        for r in range(N):
            summ += nums[r]
            while summ >= target:
                MIN = min(MIN, r-l+1)
                summ -= nums[l]
                l += 1

        return MIN if MIN != float('inf') else 0

            
