class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        S = set()
        n = len(s)
        l = 0

        for r in range(n):
            while s[r] in S:
                S.remove(s[l])
                l += 1
                
            # valid window now
            w = (r - l) + 1
            max_length = max(max_length, w)
            
            S.add(s[r])

        return max_length

