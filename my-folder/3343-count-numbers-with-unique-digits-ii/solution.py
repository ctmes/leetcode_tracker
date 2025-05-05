class Solution:
    def numberCount(self, a: int, b: int) -> int:
        acc = 0

        for num in range(a,b+1):
            S = set()
            chars = str(num)
            for char in chars:
                if char in S:
                    continue
                else:
                    S.add(char)

            if len(S) == len(chars):
                acc += 1
        return acc
