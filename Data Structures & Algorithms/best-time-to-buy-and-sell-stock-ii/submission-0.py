class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
    
        for i in range(len(prices) - 1):

            value = prices[i+1] - prices[i]
            if value > 0:
                profit += value


        return profit