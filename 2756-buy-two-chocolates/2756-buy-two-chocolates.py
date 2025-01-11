class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices=sorted(prices)
        a=money
        for i in range(2):
            a-=prices[i]
        if a>=0:
            return a
        else:
            return money