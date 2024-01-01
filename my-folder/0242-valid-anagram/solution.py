class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sD = {}
        sT = {}

        for char in s:
            if char in sD:
                sD[char] += 1
            else:
                sD[char] = 1
        
        for char in t:
            if char in sT:
                sT[char] += 1
            else:
                sT[char] = 1

        if sD == sT:
            return True
        return False
