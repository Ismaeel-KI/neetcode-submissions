class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        s = s.lower()
        t = t.lower()

        for i in s:
            arr[ord(i) - ord('a')] += 1
        print(arr)
        
        for j in t:
            arr[ord(j) - ord('a')] -= 1
        print(arr)

        if all(x == 0 for x in arr):
            return True
        else:
            return False