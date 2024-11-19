class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for r in ransomNote:
            if (r not in magazine or magazine.count(r) < ransomNote.count(r)):
                return False
        
        return True
        
