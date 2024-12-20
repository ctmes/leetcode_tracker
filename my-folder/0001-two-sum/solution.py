class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return False
        
        seen = {}
        for i, num in enumerate(nums):
            print("Printed!", i, num)
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
