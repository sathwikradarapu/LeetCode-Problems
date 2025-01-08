class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            l1=[0,1,1]
            r=n-len(l1)
            for i in range(r+1):
                num=l1[-1]+l1[-2]+l1[-3]
                l1.append(num)
            return l1[-1]