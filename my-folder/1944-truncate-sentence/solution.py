class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ls = s.split()
        out = ""

        for word in range(k-1):
            out += ls[word] + " "

        
        out += ls[k-1]

        return out

        
        
