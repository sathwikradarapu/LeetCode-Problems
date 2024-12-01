from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        hold, sold, rest = -prices[0], 0, 0  # Initialize base cases
        
        for i in range(1, n):
            new_hold = max(hold, rest - prices[i])  # Hold or buy today
            new_sold = hold + prices[i]  # Sell today
            new_rest = max(rest, sold)  # Rest or cooldown
            
            hold, sold, rest = new_hold, new_sold, new_rest  # Update states
        
        return max(sold, rest)  # Max profit on the last day

