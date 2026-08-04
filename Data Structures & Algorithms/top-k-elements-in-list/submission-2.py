class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = defaultdict(int)

        for num in nums:
            h[num] += 1

        m = []
        for _ in range(k):
            l = max(h, key=h.get)
            m.append(l)
            h.pop(l)

        return m