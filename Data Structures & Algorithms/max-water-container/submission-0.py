class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0
        j = len(heights) - 1
        m_h = 0

        while i < j:
            height = min(heights[i], heights[j])
            width = j - i
            area = height * width
            m_h = max(m_h, area)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return m_h