class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        check = {}
        for i, number in enumerate(numbers):
            val = target - number
            if val in check:
                output = [check[val], i+1]
                return output
            else:
                check[number] = i + 1
        return []