class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0

        close_b = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        while i < len(s):
            if s[i] in close_b:
                if stack and stack[-1] == close_b[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
                    
            i += 1

        if stack:
            return False
        else:
            return True
