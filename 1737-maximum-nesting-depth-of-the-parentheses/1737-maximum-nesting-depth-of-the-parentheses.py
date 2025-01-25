class Solution:
    def maxDepth(self, s: str) -> int:
        res=[]
        c1=0
        ans=float("-inf")
        for i in s:
            if i=='(':
                res.append(i)
                c1+=1
            elif i==')':
                if res[-1]=='(':
                    res.pop()
                    c1-=1
            ans=max(ans,c1)
        return ans