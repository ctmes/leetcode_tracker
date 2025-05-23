class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        ans, sol = [], []

        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
            }

        n = len(digits)

        def backtrack(i=0):
            if i == n:
                ans.append(''.join(sol))
                return ans


            for letter in d[digits[i]]:
                sol.append(letter)
                backtrack(i+1)
                sol.pop()

        backtrack(0)

        return ans

