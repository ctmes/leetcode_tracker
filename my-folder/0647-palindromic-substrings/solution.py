class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindromes(left: int, right: int) -> int:
            count = 0
            # Expand around center while within bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        total = 0
        # Check palindromes centered at each position
        for i in range(len(s)):
            # Odd-length palindromes (center at i)
            total += countPalindromes(i, i)
            # Even-length palindromes (center between i and i+1)
            if i < len(s) - 1:
                total += countPalindromes(i, i + 1)
        
        return total
