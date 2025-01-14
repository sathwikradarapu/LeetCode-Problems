class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        a=""
        b=""
        c=0
        d=0
        for i in range(n):
            if i%2==0:
                a+='0'
                b+='1'
            else:
                a+='1'
                b+='0'
        for i in range(n):
            if s[i]!=a[i]:
                c+=1
            if s[i]!=b[i]:
                d+=1
        return min(c,d)