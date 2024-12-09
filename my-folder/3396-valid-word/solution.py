class Solution:
    def isValid(self, word: str) -> bool:
        if not word:
            print('1')
            return False
        
        if len(word) < 3:
            print('2')
            return False

        for char in word:
            if char.isalnum() == False:
                print('3')
                return False

        vowels = "aeiou"
        vowels2 = "aeiou0123456789"

        # vowels > 0
        if len(set(word.lower()).intersection(vowels)) == 0:
            print(len(set(word).intersection(vowels)))
            print('4')
            return False

        # consonants > 0
        if len(set(word.lower()).difference(vowels2)) == 0:
            print('5')
            return False
        
        return True
