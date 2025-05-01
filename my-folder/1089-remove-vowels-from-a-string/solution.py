class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = "aeiou"
        out = ""

        for letter in s:
            if letter not in vowels:
                out += (letter)

        return out
