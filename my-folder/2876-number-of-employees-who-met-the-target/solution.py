class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        out = 0 

        for employee in hours:
            if employee >= target:
                out += 1

        return out
