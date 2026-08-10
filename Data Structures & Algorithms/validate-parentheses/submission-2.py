class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0

        open_b = ["{", "(", "["]
        close_b = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        while i < len(s):
            if s[i] in open_b:
                stack.append(s[i])
            else:
                if stack and stack[-1] == close_b[s[i]]:
                    stack.pop()
                else:
                    return False
                    
            i += 1
        print(stack)

        if stack:
            return False
        else:
            return True
