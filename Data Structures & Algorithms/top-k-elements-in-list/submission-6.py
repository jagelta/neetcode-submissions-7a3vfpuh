class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        print(frequency)
        max_value = 0
        max_count = float("-inf")
        output = []
        for j in range(0,k):
            for i in frequency:
                if frequency[i] > max_count:
                    max_value = i
                    max_count = frequency[i]
            output.append(max_value)
            frequency[max_value] = 0
            max_count = float("-inf")
        return output