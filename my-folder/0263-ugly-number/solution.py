class Solution:
    def prime_factors(self, n):
        factors = []

        # Divide by 2 while n is even
        while n % 2 == 0:
            factors.append(2)
            n = n // 2

        # Divide by odd numbers starting from 3
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n = n // i

        # If n is a prime number greater than 2
        if n > 2:
            factors.append(n)

        return factors

    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factors = self.prime_factors(n)

        for factor in factors:
            if factor != 2 and factor != 3 and factor != 5:
                return False

        return True

