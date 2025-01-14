class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        c=0
        for i in range(n):
            if i%2:
                if s[i]=='0':
                    c+=1
            else:
                if s[i]=='1':
                    c+=1
        return min(c,n-c)