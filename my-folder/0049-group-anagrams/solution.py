class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            # Use setdefault to initialize empty list if key doesn't exist
            d.setdefault(sorted_word, []).append(word)
        
        return list(d.values())
