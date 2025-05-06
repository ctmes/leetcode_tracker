class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        running = 0

        for num in nums:
            running += num
            out.append(running)

        return out
