class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=float("-inf")
        i=0
        n=len(height)
        j=n-1
        while i<n and j>=i:
            a=height[i]
            b=height[j]
            c=min(a,b)
            d=j-i
            e=c*d
            ans=max(ans,e)
            if c==a:
                i+=1
            elif c==b:
                j-=1
            elif a==b:
                i+=1
                j-=1
        return ans