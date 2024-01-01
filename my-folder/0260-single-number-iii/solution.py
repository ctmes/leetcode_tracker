class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        ans = []

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        for k, v in d.items():
            if v == 1:
                ans.append(k)

        return ans
