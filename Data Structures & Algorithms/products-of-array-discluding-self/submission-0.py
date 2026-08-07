class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [1] * (len(nums))
        pre = 1
        suf = 1

        for i in range(0, len(nums) - 1):
            pre *= nums[i]
            r[i + 1] = pre

        for i in range(len(nums) - 1, 0, -1):
            suf *= nums[i]
            r[i - 1] *= suf
            
        return r