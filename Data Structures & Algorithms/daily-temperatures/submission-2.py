class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackind, temp = stack.pop()
                res[stackind] = i - stackind
            stack.append((i, t))
        return res
            