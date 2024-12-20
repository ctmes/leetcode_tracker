class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return False

        n = len(nums)

        products = [1] * n

        #for prefix
        prefix = 1
        for i in range(n):
            products[i] = prefix
            prefix *= nums[i]

        #for suffix
        suffix = 1
        for i in range(n-1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]

        return products
