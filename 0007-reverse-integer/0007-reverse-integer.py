class Solution:
    def reverse(self, x: int) -> int:
        y=abs(x)
        y=str(y)[::-1]
        y=int(y)
        if x<0:
            y=-y
        if y<(-2**31) or y>(2**31-1):
            y=0
        return y