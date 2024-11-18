class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        minimum = min(len(word1), len(word2))
        for i in range(minimum):
            output += word1[i]
            output += word2[i]
        output += word1[minimum:]
        output += word2[minimum:]

        return output
