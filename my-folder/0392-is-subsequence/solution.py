class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            if t.count(char) == 0:
                return False

        if len(s) == len(t) and s != t:
            return False

        if s == "":
            return True

        for char in s:
            charFlag = False
            for tChar in t:
                if char == tChar:
                    t = t[t.index(tChar)+1:]
                    charFlag = True
                    break

            if not charFlag:
                return False
        return True


