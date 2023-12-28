class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = None
        count = 0

        for num in nums:
            if count == 0:
                curr = num
            count += 1 if num == curr else -1

        return curr
