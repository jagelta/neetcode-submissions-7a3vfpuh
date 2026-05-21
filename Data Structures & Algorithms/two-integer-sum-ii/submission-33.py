class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # check = {}
        # for i, number in enumerate(numbers):
        #     val = target - number
        #     if val in check:
        #         output = [check[val], i+1]
        #         return output
        #     else:
        #         check[number] = i + 1
        # return []
        lp = len(numbers) -1
        rp = 0
        while lp > rp:
            if numbers[rp] + numbers[lp] > target:
                lp -= 1
            elif numbers[rp] + numbers[lp] < target:
                rp += 1
            else:
                return [rp+1, lp+1]
        return []