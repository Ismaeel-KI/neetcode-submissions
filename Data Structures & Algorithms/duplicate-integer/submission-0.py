class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l_list = len(nums)
        l_set = len(set(nums))

        if l_list == l_set:
            return False
        else:
            return True 