class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seta = set(nums)



        if len(nums) != len(seta):
            return True
        return False
