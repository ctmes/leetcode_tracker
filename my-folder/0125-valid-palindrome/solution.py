class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = [char.upper() for char in s if char.isalnum()]
        l = 0
        r = len(cs) - 1

        while l <= r:
            if cs[l] == cs[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True
