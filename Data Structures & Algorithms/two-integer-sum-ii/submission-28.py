class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        check = {}
        for i, number in enumerate(numbers):
            val = target - number
            print(val)
            if val in check:
                print(number)
                output = [check[val], i+1]
                print(check)
                return output
            else:
                check[number] = i + 1
        print(check)
        return []