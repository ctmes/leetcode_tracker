class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        big_word_1 = ""
        big_word_2 = ""

        for word in word1:
            big_word_1 += word

        for word in word2:
            big_word_2 += word

        return big_word_1 == big_word_2
