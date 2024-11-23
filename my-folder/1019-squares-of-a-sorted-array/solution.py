class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return False

        nums2 = [pow(num,2) for num in nums]
        return sorted(nums2)
        
