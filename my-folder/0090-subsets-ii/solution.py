class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to handle duplicates
        res, sol = [], []
        n = len(nums)

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            # Include the current number
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

            # Skip duplicates to avoid duplicate subsets
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            
            # Exclude the current number and move to the next distinct number
            backtrack(i + 1)

        backtrack(0)
        return res
