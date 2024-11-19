class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bC = text.count("b")
        aC = text.count("a")
        lC = text.count("l")
        oC = text.count("o")
        nC = text.count("n")
        balloons = 0

        while bC >= 1 and aC >= 1 and lC >= 2 and oC>= 2 and nC>= 1:
            balloons += 1
            bC -= 1
            aC -= 1
            lC -= 2
            oC -= 2
            nC -= 1

        else:
            return balloons
