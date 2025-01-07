class Solution:
    def countOdds(self, low: int, high: int) -> int:
        dis=high-low+1
        if dis%2==0:
            return dis//2
        else:
            if dis%2 and (low%2 or high%2):
                return dis//2+1
            else:
                return dis//2