class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = []
        for i in s:
            if i.isalnum():
                s_.append(i.lower())

        i, j = 0, len(s_) - 1

        while i < j:
            if s_[i] != s_[j]:
                return False
            i += 1
            j -= 1
        return True