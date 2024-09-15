class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval=prices[0]
        ans=0
        for i in range(len(prices)):
            minval=min(prices[i],minval)
            ans=max(ans,(prices[i]-minval))
        return ans