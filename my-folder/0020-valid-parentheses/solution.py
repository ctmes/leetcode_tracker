class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) < 2:
            return False

        for c in s:
            if c in "([{":
                stack.append(c)
            
            elif c == ")":
                if not stack or stack.pop() != "(":
                    return False

            elif c == "}":
                if not stack or stack.pop() != "{":
                    return False

            elif c == "]":
                if not stack or stack.pop() != "[":
                    return False

        if stack:
            return False

        return True
        
