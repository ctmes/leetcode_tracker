class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = {}

        for char in magazine:
            if char in s:
                s[char] += 1
            else:
                s[char] = 1
        
        for char in ransomNote:
            if char in s:
                s[char] -= 1
            else:
                return False

        for char in s:
            if s[char] < 0:
                return False

        return True
        
