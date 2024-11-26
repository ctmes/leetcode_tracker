class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for c in operations:
            if c != "+" and c != "D" and c != "C":
                record.append(int(c))
            elif c == "C":
                record.pop()
            elif c == "D":
                record.append(record[-1] * 2)
            elif c == "+":
                record.append(record[-1] + record[-2])
        
        return sum(record)

