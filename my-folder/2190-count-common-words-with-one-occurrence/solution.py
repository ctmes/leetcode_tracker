class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ans = 0

        for word in words1:
            if words1.count(word) == 1:
                if word in words2:
                    if words2.count(word) == 1:
                        ans += 1
        
        return ans
