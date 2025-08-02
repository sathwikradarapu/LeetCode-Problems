class Solution:
    def fib(self, n: int) -> int:
        if n<=0:
            return 0
        else:
            a=[0,1]
            if n==1:
                return a[1]
            elif n==2:
                return a[0]+a[1]
            else:
                m=n-len(a)
                for i in range(m):
                    b=a[-1]+a[-2]
                    a.append(b)
                return a[n-1]+a[n-2]