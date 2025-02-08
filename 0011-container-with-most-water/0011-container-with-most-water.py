class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=float("-inf")
        n=len(height)
        l=0
        r=n-1
        while l<r:
            a=height[l]
            b=height[r]
            c=min(a,b)
            d=abs(l-r)
            e=c*d
            ans=max(ans,e)
            if a<b:
                l+=1
            else:
                r-=1
        return ans