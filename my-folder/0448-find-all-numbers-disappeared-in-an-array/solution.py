class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        A = set(nums)
        B = set([i for i in range(1, len(nums) + 1)])
        
        return list(B.difference(A))
