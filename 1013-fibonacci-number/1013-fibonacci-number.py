class Solution:
    def fib(self, n: int) -> int:
        def fibonacci(n):
            nonlocal a,b
            if n<=0:
                return 
            elif n==1:
                return 
            else:
                a,b=b,a+b
                n=n-1
                fibonacci(n)
        a=0
        b=1
        if n<=0:
            return 0
        elif n==1:
            return 1
        else:
            fibonacci(n)
            return b