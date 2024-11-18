class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        iv = s.count("IV")
        ix = s.count("IX")
        xl = s.count("XL")
        xc = s.count("XC")
        cd = s.count("CD")
        cm = s.count("CM")

        i = s.count("I") - iv - ix
        v = s.count("V") - iv
        x = s.count("X") - ix - xl - xc
        l = s.count("L") - xl
        c = s.count("C") - xc - cd - cm
        d = s.count("D") - cd
        m = s.count("M") - cm

        sum += 4 * iv + 9 * ix + 40 * xl + 90 * xc + 400 * cd + 900 * cm + i + 5 * v + 10 * x + 50 * l + 100 * c + 500 * d + 1000 * m
        return sum
