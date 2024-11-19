class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # for char in s:
        #     try:
        #         t.remove(char)
        #     except:
        #         return False

        if sorted(s) == sorted(t):
            return True
        return False
