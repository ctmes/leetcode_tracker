class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1

        max_so_far = 0

        while l < r:
            tallest = min(height[l], height[r])
            max_so_far = max(max_so_far, (tallest * (r-l)))
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_so_far

        
