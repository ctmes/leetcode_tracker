class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return False
        
        # Use a dictionary to store the complement and its index
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

