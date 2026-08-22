class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        a = 0

        l_m = 0
        r_m = 0

        while i < j:
            if height[i] <= height[j]:
                if height[i] >= l_m:
                    l_m = height[i]
                else:
                    a += l_m - height[i]

                i += 1

            else:
                if height[j] >= r_m:
                    r_m = height[j]
                else:
                    a += r_m - height[j]

                j -= 1
        
        return a

            
            