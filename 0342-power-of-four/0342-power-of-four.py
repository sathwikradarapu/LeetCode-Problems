class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i=0
        x=(4**i)
        while x<=n:
            x=(4**i)
            if x==n:
                return True
            i+=1
        return False