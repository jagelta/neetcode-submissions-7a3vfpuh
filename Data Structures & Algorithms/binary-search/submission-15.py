class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while high >= low:
            mid = (high-low)//2+low
            if target>nums[mid]:
                low = mid + 1
            elif target<nums[mid]:
                high = mid-1
            elif target == nums[mid]:
                return mid
        return -1
        