class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        DICT = {}
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if (pattern[i], words[i]) in DICT.items():
                continue
            elif (pattern[i], words[i]) not in DICT.items() and \
            (pattern[i] in DICT.keys()):
                return False
            elif (pattern[i], words[i]) not in DICT.items() and \
            (words[i] in DICT.values()):
                return False
            else:
                DICT[pattern[i]] = words[i]

        return True


        
