class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        olds = []
        out = []

        for num in nums:
            if num in olds:
                out.append(num)
            else:
                olds.append(num)

        return out
