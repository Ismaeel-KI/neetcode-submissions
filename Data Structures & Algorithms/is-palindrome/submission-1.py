class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        s = s.lower()
        i, j = 0, length - 1

        while i < j:
            print(s[i], s[j])
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True