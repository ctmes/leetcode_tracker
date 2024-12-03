class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        word = ""
        ls = []
        for digit in digits:
            word += str(digit)

        num = int(word)

        num += 1

        word = str(num)

        for letter in word:
            ls.append(int(letter))

        return ls
