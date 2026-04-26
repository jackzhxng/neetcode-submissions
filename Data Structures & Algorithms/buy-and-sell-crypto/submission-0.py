class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time taken: 4 min
        """
        lowest = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            price = prices[i]
            max_profit = max(max_profit, price - lowest)
            lowest = min(lowest, price)
        return max_profit