class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        for i in range(n):
            if 2**i==n:
                return True
            if 2**i>n:
                return False
            