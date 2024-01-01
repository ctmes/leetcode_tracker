class Solution:
    def addDigits(self, num: int) -> int:
        n = sum(int(digit) for digit in str(num))
            
        if n > 9:
            n = self.addDigits(n)

        return n
