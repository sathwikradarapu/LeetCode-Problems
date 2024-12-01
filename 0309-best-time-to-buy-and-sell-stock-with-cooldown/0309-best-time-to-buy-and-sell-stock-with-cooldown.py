from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        # Initialize DP arrays
        hold = [0] * n  # Max profit holding stock on day i
        sold = [0] * n  # Max profit just sold stock on day i
        rest = [0] * n  # Max profit doing nothing on day i
        
        # Base cases
        hold[0] = -prices[0]  # Buy stock on the first day
        sold[0] = 0  # Cannot sell on the first day
        rest[0] = 0  # Rest state on the first day
        
        for i in range(1, n):
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])  # Hold or buy today
            sold[i] = hold[i - 1] + prices[i]  # Sell today
            rest[i] = max(rest[i - 1], sold[i - 1])  # Do nothing or cooldown
        
        # Max profit is either we are in rest or just sold state on the last day
        return max(sold[n - 1], rest[n - 1])
