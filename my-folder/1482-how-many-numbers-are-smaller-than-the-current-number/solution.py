class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out = []
        sorted_nums = sorted(nums)

        for num in nums:
            out.append(sorted_nums.index(num))

        return out



