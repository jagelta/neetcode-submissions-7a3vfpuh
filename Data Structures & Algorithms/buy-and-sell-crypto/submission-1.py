class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = prices[0]
        for i in prices:
            if i < min:
                min = i
            value = i - min
            if value > profit:
                profit = value
        return profit

        