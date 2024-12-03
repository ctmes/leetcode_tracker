class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum: int = nums[0]
        cur_sum: int = nums[0]
        for right in range(1, len(nums)):
            cur_sum = max(cur_sum + nums[right], nums[right])
            max_sum = max(max_sum, cur_sum)
        return max_sum
