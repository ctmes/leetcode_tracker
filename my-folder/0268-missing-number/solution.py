class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        f = factorial(len(nums))
        product = 1
        zero_present = False

        for i in nums:
            if i == 0:
                zero_present = True
            else:
                product *= i

        if zero_present:
            return int(f / product)
        return 0
