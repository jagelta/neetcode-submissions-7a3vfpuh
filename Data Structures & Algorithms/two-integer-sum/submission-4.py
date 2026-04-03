class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            for index, x in enumerate(nums):
                for idx, y in enumerate(nums[index+1:]):
                    if x + y == target:
                        return [index, idx + index + 1]
