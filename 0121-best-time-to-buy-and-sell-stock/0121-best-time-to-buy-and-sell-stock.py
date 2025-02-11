class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mini=float("inf")
        ans=float("-inf")
        for i in range(n):
            mini=min(prices[i],mini)
            ans=max(ans,(prices[i]-mini))
        return ans