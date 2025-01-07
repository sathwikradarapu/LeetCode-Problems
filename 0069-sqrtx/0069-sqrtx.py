class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        if x==2:
            return x-1
        for i in range(x):
            val=i*i
            if val==x:
                return i
            if val>x:
                return i-1