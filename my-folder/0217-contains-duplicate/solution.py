class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        numsetlist = list(numset)

        if len(nums) != len(numset):
            return True
        return False
