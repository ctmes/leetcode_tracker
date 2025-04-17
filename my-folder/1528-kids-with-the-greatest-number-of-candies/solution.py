class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []

        for c in candies:
            if max(candies) <= c + extraCandies:
                out.append(True)
            else:
                out.append(False)

        return out

