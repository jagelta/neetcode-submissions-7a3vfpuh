class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i, num in enumerate(nums):
            lp = len(nums)-1
            rp = i+1
            while lp > rp:
                if nums[rp] + nums[lp] > -num:
                    lp -= 1
                elif nums[rp] + nums[lp] < -num:
                    rp += 1
                else:
                    item = [nums[rp], nums[i], nums[lp]]
                    if item not in output:
                        output.append(item)
                    lp -= 1
                    rp += 1
        return output
                    