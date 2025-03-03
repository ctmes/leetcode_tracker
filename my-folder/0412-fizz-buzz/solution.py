class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []

        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                out.append("FizzBuzz")
            elif num % 3 == 0:
                out.append("Fizz")
            elif num % 5 == 0:
                out.append("Buzz")
            else:
                out.append(f"{num}")

        return out
