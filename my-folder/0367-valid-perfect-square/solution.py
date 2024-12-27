class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num - 1

        if num == 1:
            return True

        while l < r:
            m = (l+r) // 2

            if  m * m == num:
                return True
            elif m * m > num:
                r = m  
            else:
                l = m + 1

        return False
        
