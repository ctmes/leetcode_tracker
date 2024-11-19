class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens = [len(s) for s in strs]
        shortest = min(strs)
        
        strs = sorted(strs)
        # for s in strs[1:]:
        #     if s[:len(shortest)] == shortest:
        #         return shortest

        for s in strs:
            for char in range(len(shortest)):
                if s[:len(shortest)] != shortest:
                    shortest = shortest[:-1]

        return shortest


