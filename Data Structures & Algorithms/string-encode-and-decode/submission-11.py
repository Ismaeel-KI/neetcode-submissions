class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for x in strs:
            code = str(len(x))
            word = code + "#" + x
            encoded += word
        print(encoded)
        return encoded
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            l = int(s[i:j])
            start = j + 1
            end = start + l 
            strs.append(s[start: end])
            
            i = end
        print(strs)
        return strs
