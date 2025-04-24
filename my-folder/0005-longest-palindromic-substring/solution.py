class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if not s or n < 1:
            return ""

        start, end = 0,0

        def helper(l: int, r: int) -> int:
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r-l-1

        for i in range(n):
            length1 = helper(i, i)
            length2 = helper(i, i + 1)
            max_length = max(length1, length2)

            if max_length > end - start:
                start = i - (max_length -1) // 2
                end = i + (max_length // 2)

        return s[start:end + 1]

            
