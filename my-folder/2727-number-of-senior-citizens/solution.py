class Solution:
    def countSeniors(self, details: List[str]) -> int:
        out = 0

        for p in details:
            if int(p[-4:-2]) > 60:
                out += 1

        return out
