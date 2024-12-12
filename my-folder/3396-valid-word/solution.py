class Solution:
    def isValid(self, word: str) -> bool:
        if not word:
            return False
        
        if len(word) < 3:
            return False

        for char in word:
            if char.isalnum() == False:
                return False

        vowels = "aeiou"
        vowels2 = "aeiou0123456789"

        # vowels > 0
        if len(set(word.lower()).intersection(vowels)) == 0:
            return False

        # consonants > 0
        if len(set(word.lower()).difference(vowels2)) == 0:
            return False
        
        return True
