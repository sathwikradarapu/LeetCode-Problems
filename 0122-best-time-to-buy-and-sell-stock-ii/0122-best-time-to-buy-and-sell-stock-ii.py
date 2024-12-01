class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
    
        # Traverse through the prices array
        for i in range(1, len(prices)):
            # If the current price is greater than the previous one, make a profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        # Return the total profit
        return profit