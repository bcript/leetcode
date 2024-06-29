class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]    # intialise the first index as the buy
        profit = 0
        for i in range(1, len(prices)):
            # if current price is lower, becomes new buy
            if prices[i] < buy:
                buy = prices[i]
            # if current price minus buy is greater than old profit, becomes new profit
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
