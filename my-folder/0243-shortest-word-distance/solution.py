class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos1, pos2 = -1, -1
        min_dist = float('inf')
        
        for i, word in enumerate(wordsDict):
            if word == word1:
                pos1 = i
                if pos2 != -1:
                    min_dist = min(min_dist, pos1 - pos2)
            elif word == word2:
                pos2 = i
                if pos1 != -1:
                    min_dist = min(min_dist, pos2 - pos1)
        
        return min_dist
